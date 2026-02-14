import pandas as pd

print("Proje başladı 🚀")

file_path = "data/raw/cicids.csv"

df = pd.read_csv(file_path, nrows=50000)

print("Veri başarıyla yüklendi ✅")
print("Boyut:", df.shape)

print("\nİlk 5 satır:")
print(df.head())

print("\nKolonlar:")
print(df.columns)

# Kolon isimlerindeki boşlukları temizle
df.columns = df.columns.str.strip()

print("\nTemizlenmiş kolonlar:")
print(df.columns)

# Label dağılımını görelim
print("\nLabel dağılımı:")
print(df["Label"].value_counts())

# Label'ı binary yapalım
df["Label"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

print("\nBinary Label dağılımı:")
print(df["Label"].value_counts())

import numpy as np

# Infinity değerleri NaN yap
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# NaN olan satırları sil
df.dropna(inplace=True)

print("\nTemizlik sonrası boyut:", df.shape)


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Feature ve label ayırma
X = df.drop("Label", axis=1)
y = df["Label"]

# Train/Test bölme
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTrain/Test bölündü ✅")

# Model oluşturma
model = RandomForestClassifier(n_estimators=50, random_state=42)

# Modeli eğit
model.fit(X_train, y_train)

print("Model eğitildi ✅")

# Tahmin yap
y_pred = model.predict(X_test)

# Sonuçlar
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
