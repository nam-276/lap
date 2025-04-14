import mlflow
import optuna
import json
import os
import argparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

def load_data():
    df = pd.read_csv("data/processed/train.csv")
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def objective(trial):
    X_train, X_test, y_train, y_test = load_data()

    params = {
        "n_estimators": trial.suggest_int("n_estimators", 50, 200),
        "max_depth": trial.suggest_int("max_depth", 3, 20),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 10),
    }

    clf = RandomForestClassifier(**params)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    # MLflow logging
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", acc)

    # Save model & metrics
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/model.pkl")
    with open("metrics.json", "w") as f:
        json.dump({"accuracy": acc}, f)

    # Save for DVC plot
    os.makedirs("plots", exist_ok=True)
    with open("plots/metrics.csv", "w") as f:
        f.write("epoch,accuracy\n1,{}\n".format(acc))

    return acc

def main():
    mlflow.set_experiment("Telco Churn - RandomForest")
    with mlflow.start_run():
        study = optuna.create_study(direction="maximize")
        study.optimize(objective, n_trials=10)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args = parser.parse_args()
    main()
