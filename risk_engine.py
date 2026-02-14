import joblib
import pandas as pd

model = joblib.load("models/ids_model.pkl")

# Modelin feature isimlerini al
feature_names = model.feature_names_in_

def evaluate_traffic(sample):

    # Sample'ı DataFrame yap
    sample_df = pd.DataFrame([sample], columns=feature_names)

    prob = model.predict_proba(sample_df)[0][1]

    if prob > 0.90:
        severity = "CRITICAL"
    elif prob > 0.70:
        severity = "HIGH"
    elif prob > 0.40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "attack_probability": round(float(prob), 3),
        "severity": severity,
        "is_attack": int(prob > 0.5)
    }
