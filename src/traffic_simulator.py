import pandas as pd
import numpy as np
import random

# Datasetten örnek veri çekerek simülasyon yapacağız
file_path = "data/raw/cicids.csv"

df = pd.read_csv(file_path, nrows=50000)
df.columns = df.columns.str.strip()

# Label hariç feature listesi
feature_columns = df.drop("Label", axis=1).columns


def generate_traffic_sample():

    # Datasetten rastgele bir satır al
    random_row = df.sample(1)

    sample = random_row[feature_columns].values[0]

    return sample
