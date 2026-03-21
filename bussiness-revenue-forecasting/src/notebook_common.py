import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

csv_path = "../data/row/business_revenue_forecasting.csv"
preview_rows = 5

target_col = "revenue"
time_col = "date"
feature_cols = [
    "num_active_users",
    "marketing_spend",
    "discount_rate",
    "new_signups",
]

def load_preview_df():
    return pd.read_csv(csv_path, nrows=preview_rows)

def load_df():
    df = pd.read_csv(csv_path)
    df[time_col] = pd.to_datetime(df[time_col], errors="coerce")
    df = df.dropna(subset=[time_col]).sort_values(time_col).reset_index(drop=True)
    return df
