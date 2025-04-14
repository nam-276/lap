import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", lr)
    mlflow.log_param("batch_size", batch_size)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_artifact("metrics.json")
    mlflow.log_artifact("models/model.pkl")
