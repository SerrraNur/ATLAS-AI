import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Dataset yolu
file_path = "data/raw/cicids.csv"

print("Veri yükleniyor...")

df = pd.read_csv(file_path, nrows=50000)

# Kolon temizleme
df.columns = df.columns.str.strip()

# Binary label
df["Label"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

# Infinity temizleme
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Feature/Label ayırma
X = df.drop("Label", axis=1)
y = df["Label"]

# Train/Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Modeli kaydet
joblib.dump(model, "models/ids_model.pkl")

print("Model kaydedildi: models/ids_model.pkl")
