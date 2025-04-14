import pandas as pd
import os
import argparse
from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    # Xử lý missing values
    df = df.dropna()

    # Encode categorical variables
    for col in df.select_dtypes(include="object").columns:
        if col != "customerID":
            df[col] = LabelEncoder().fit_transform(df[col])

    df.drop("customerID", axis=1, inplace=True)
    return df

def main(config_path):
    os.makedirs("data/processed", exist_ok=True)

    # Load raw data
    df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    # Preprocess
    df_clean = preprocess(df)

    # Save processed
    df_clean.to_csv("data/processed/train.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args = parser.parse_args()

    main(args.config)
