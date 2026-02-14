import streamlit as st
import time
import pandas as pd
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from traffic_simulator import generate_traffic_sample
from risk_engine import evaluate_traffic

st.set_page_config(page_title="AI SOC Dashboard", layout="wide")

st.title("🛡 AI-Powered Intrusion Detection System")

if "logs" not in st.session_state:
    st.session_state.logs = []

col1, col2, col3, col4 = st.columns(4)

run_button = st.button("Start Monitoring")

if run_button:
    for _ in range(30):

        sample = generate_traffic_sample()
        result = evaluate_traffic(sample)

        log_entry = {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Probability": result["attack_probability"],
            "Severity": result["severity"],
            "Attack": result["is_attack"]
        }

        st.session_state.logs.append(log_entry)

        time.sleep(0.3)

df_logs = pd.DataFrame(st.session_state.logs)

if not df_logs.empty:

    total_attacks = df_logs["Attack"].sum()
    last_severity = df_logs.iloc[-1]["Severity"]

    col1.metric("Total Traffic", len(df_logs))
    col2.metric("Total Attacks", int(total_attacks))
    col3.metric("Attack Ratio (%)", round((total_attacks / len(df_logs)) * 100, 2))
    col4.metric("Last Severity", last_severity)

    st.subheader("🚨 Active Threat Level")

    if last_severity == "CRITICAL":
        st.error("🔴 CRITICAL THREAT DETECTED")
    elif last_severity == "HIGH":
        st.warning("🟠 HIGH RISK TRAFFIC")
    elif last_severity == "MEDIUM":
        st.warning("🟡 MEDIUM RISK TRAFFIC")
    else:
        st.success("🟢 SYSTEM STABLE")

    st.subheader("📊 Severity Distribution")
    severity_counts = df_logs["Severity"].value_counts()
    st.bar_chart(severity_counts)

    st.subheader("📈 Attack Probability Trend")
    st.line_chart(df_logs["Probability"])

    st.subheader("📜 Traffic Logs")
    st.dataframe(df_logs, use_container_width=True)
