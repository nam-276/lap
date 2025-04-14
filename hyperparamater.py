import optuna
import mlflow

def objective(trial):
    lr = trial.suggest_float("lr", 1e-4, 1e-1, log=True)
    batch_size = trial.suggest_int("batch_size", 16, 128)

    with mlflow.start_run():
        acc = train_model(lr, batch_size)
        mlflow.log_params({"lr": lr, "batch_size": batch_size})
        mlflow.log_metric("accuracy", acc)

    return acc

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=20)
