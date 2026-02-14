from traffic_simulator import generate_traffic_sample
from risk_engine import evaluate_traffic

print("Sistem test ediliyor...\n")

for i in range(5):
    sample = generate_traffic_sample()
    result = evaluate_traffic(sample)

    print(f"Traffic {i+1}")
    print(result)
    print("-" * 40)
