import pandas as pd
import joblib
import argparse
import os
from sklearn.metrics import classification_report, confusion_matrix

def main(config_path):
    # Load data
    df = pd.read_csv("data/processed/train.csv")
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Load model
    model = joblib.load("models/model.pkl")

    # Predict & evaluate
    y_pred = model.predict(X)

    report = classification_report(y, y_pred, output_dict=True)
    matrix = confusion_matrix(y, y_pred)

    # Save report
    os.makedirs("reports", exist_ok=True)
    with open("reports/classification_report.txt", "w") as f:
        f.write(classification_report(y, y_pred))

    with open("reports/confusion_matrix.txt", "w") as f:
        f.write(str(matrix))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args = parser.parse_args()

    main(args.config)
