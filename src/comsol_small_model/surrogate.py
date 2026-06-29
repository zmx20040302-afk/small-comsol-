from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
import warnings


@dataclass(frozen=True)
class TrainReport:
    best_model: str
    train_rmse: float
    test_rmse: float
    test_mae: float
    test_r2: float
    rows: int
    input_columns: list[str]
    output_columns: list[str]
    train_rows: int
    test_rows: int
    candidate_reports: list[dict[str, Any]]
    per_output_metrics: dict[str, dict[str, float]]
    data_quality: dict[str, Any]
    feature_stats: dict[str, dict[str, float]]
    output_stats: dict[str, dict[str, float]]
    sample_predictions: list[dict[str, Any]]
    training_summary: list[str]
    recommendations: list[str]
    warnings: list[str]


def train_surrogate(
    csv_path: str | Path,
    model_path: str | Path,
    input_columns: list[str],
    output_columns: list[str],
    random_state: int = 42,
) -> TrainReport:
    data = pd.read_csv(csv_path)
    missing = [col for col in input_columns + output_columns if col not in data.columns]
    if missing:
        raise ValueError(f"CSV missing required columns: {', '.join(missing)}")
    report_warnings = _dataset_warnings(data, input_columns, output_columns)

    x = data[input_columns].to_numpy(dtype=float)
    y = data[output_columns].to_numpy(dtype=float)
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("CSV contains NaN or infinite values in selected input/output columns")

    test_size = 0.2 if len(data) >= 20 else 0.33
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state
    )

    candidates = _candidate_models(len(data), random_state)
    candidate_reports = []
    fitted_models = {}
    for name, model in candidates:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", ConvergenceWarning)
            model.fit(x_train, y_train)
        convergence_warnings = [
            "MLP did not fully converge. Add more data, reduce model size, or increase max_iter."
            for warning in caught
            if issubclass(warning.category, ConvergenceWarning)
        ]
        report_warnings.extend(convergence_warnings)
        train_pred = model.predict(x_train)
        test_pred = model.predict(x_test)
        candidate_reports.append(
            {
                "name": name,
                "train_rmse": _rmse(y_train, train_pred),
                "test_rmse": _rmse(y_test, test_pred),
                "test_mae": float(mean_absolute_error(y_test, test_pred)),
                "test_r2": _safe_r2(y_test, test_pred),
                "warnings": convergence_warnings,
            }
        )
        fitted_models[name] = model

    best = _best_candidate(candidate_reports)
    model = fitted_models[best["name"]]
    train_pred = model.predict(x_train)
    test_pred = model.predict(x_test)
    sample_predictions = _sample_predictions(y_test, test_pred, output_columns)
    payload = {
        "model": model,
        "model_name": best["name"],
        "input_columns": input_columns,
        "output_columns": output_columns,
        "candidate_reports": candidate_reports,
        "data_quality": _data_quality(data, input_columns, output_columns),
    }
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(payload, model_path)

    return TrainReport(
        best_model=best["name"],
        train_rmse=_rmse(y_train, train_pred),
        test_rmse=_rmse(y_test, test_pred),
        test_mae=float(mean_absolute_error(y_test, test_pred)),
        test_r2=_safe_r2(y_test, test_pred),
        rows=len(data),
        input_columns=list(input_columns),
        output_columns=list(output_columns),
        train_rows=len(x_train),
        test_rows=len(x_test),
        candidate_reports=candidate_reports,
        per_output_metrics=_per_output_metrics(y_test, test_pred, output_columns),
        data_quality=_data_quality(data, input_columns, output_columns),
        feature_stats=_column_stats(data, input_columns),
        output_stats=_column_stats(data, output_columns),
        sample_predictions=sample_predictions,
        training_summary=_training_summary(best, candidate_reports, len(data), input_columns, output_columns),
        recommendations=_recommendations(len(data), best, report_warnings),
        warnings=_dedupe(report_warnings),
    )


def predict(model_path: str | Path, inputs: list[float]) -> dict[str, float]:
    payload = joblib.load(model_path)
    input_columns = payload["input_columns"]
    output_columns = payload["output_columns"]
    if len(inputs) != len(input_columns):
        raise ValueError(f"Expected {len(input_columns)} inputs: {', '.join(input_columns)}")

    prediction = payload["model"].predict(np.asarray([inputs], dtype=float))[0]
    return {name: float(value) for name, value in zip(output_columns, prediction)}


def _rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(mean_squared_error(y_true, y_pred) ** 0.5)


def _candidate_models(rows: int, random_state: int) -> list[tuple[str, Any]]:
    hidden_layers = (24, 24) if rows < 100 else (64, 64)
    return [
        ("dummy_mean_baseline", DummyRegressor(strategy="mean")),
        (
            "ridge_scaled",
            TransformedTargetRegressor(
                regressor=Pipeline([("x_scale", StandardScaler()), ("ridge", Ridge(alpha=1.0))]),
                transformer=StandardScaler(),
            ),
        ),
        (
            "random_forest",
            RandomForestRegressor(
                n_estimators=160,
                min_samples_leaf=2 if rows >= 40 else 1,
                random_state=random_state,
            ),
        ),
        (
            "mlp_scaled",
            TransformedTargetRegressor(
                regressor=Pipeline(
                    steps=[
                        ("x_scale", StandardScaler()),
                        (
                            "mlp",
                            MLPRegressor(
                                hidden_layer_sizes=hidden_layers,
                                activation="relu",
                                alpha=1e-4,
                                early_stopping=rows >= 50,
                                validation_fraction=0.15,
                                learning_rate_init=1e-3,
                                max_iter=2500,
                                random_state=random_state,
                            ),
                        ),
                    ]
                ),
                transformer=StandardScaler(),
            ),
        ),
    ]


def _best_candidate(candidate_reports: list[dict[str, Any]]) -> dict[str, Any]:
    non_baseline = [item for item in candidate_reports if item["name"] != "dummy_mean_baseline"]
    pool = non_baseline or candidate_reports
    return min(pool, key=lambda item: item["test_rmse"])


def _safe_r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    try:
        score = r2_score(y_true, y_pred, multioutput="variance_weighted")
    except ValueError:
        return float("nan")
    return float(score)


def _per_output_metrics(y_true: np.ndarray, y_pred: np.ndarray, output_columns: list[str]) -> dict[str, dict[str, float]]:
    metrics = {}
    for index, name in enumerate(output_columns):
        actual = y_true[:, index]
        predicted = y_pred[:, index]
        metrics[name] = {
            "rmse": _rmse(actual, predicted),
            "mae": float(mean_absolute_error(actual, predicted)),
            "r2": _safe_r2(actual.reshape(-1, 1), predicted.reshape(-1, 1)),
        }
    return metrics


def _data_quality(data: pd.DataFrame, input_columns: list[str], output_columns: list[str]) -> dict[str, Any]:
    selected = input_columns + output_columns
    return {
        "rows": int(len(data)),
        "columns": list(data.columns),
        "selected_columns": selected,
        "missing_values": {column: int(data[column].isna().sum()) for column in selected},
        "duplicate_rows": int(data.duplicated(subset=selected).sum()),
        "input_columns": list(input_columns),
        "output_columns": list(output_columns),
    }


def _dataset_warnings(data: pd.DataFrame, input_columns: list[str], output_columns: list[str]) -> list[str]:
    warnings_list = []
    if len(data) < 20:
        warnings_list.append(
            f"Dataset has only {len(data)} rows. This is enough for a smoke test, but not enough for a reliable surrogate model."
        )
    selected = input_columns + output_columns
    duplicate_count = int(data.duplicated(subset=selected).sum())
    if duplicate_count:
        warnings_list.append(f"Dataset has {duplicate_count} duplicate selected rows.")
    for column in selected:
        if data[column].isna().any():
            warnings_list.append(f"Column {column} contains missing values.")
        if pd.to_numeric(data[column], errors="coerce").nunique(dropna=True) <= 1:
            warnings_list.append(f"Column {column} has one or fewer unique numeric values.")
    return warnings_list


def _column_stats(data: pd.DataFrame, columns: list[str]) -> dict[str, dict[str, float]]:
    stats = {}
    for column in columns:
        series = pd.to_numeric(data[column], errors="coerce")
        stats[column] = {
            "min": float(series.min()),
            "max": float(series.max()),
            "mean": float(series.mean()),
            "std": float(series.std(ddof=0)),
        }
    return stats


def _sample_predictions(y_true: np.ndarray, y_pred: np.ndarray, output_columns: list[str], limit: int = 5) -> list[dict[str, Any]]:
    rows = []
    for index in range(min(limit, len(y_true))):
        rows.append(
            {
                "actual": {name: float(value) for name, value in zip(output_columns, y_true[index])},
                "predicted": {name: float(value) for name, value in zip(output_columns, y_pred[index])},
                "absolute_error": {
                    name: float(abs(actual - predicted))
                    for name, actual, predicted in zip(output_columns, y_true[index], y_pred[index])
                },
            }
        )
    return rows


def _training_summary(
    best: dict[str, Any],
    candidate_reports: list[dict[str, Any]],
    rows: int,
    input_columns: list[str],
    output_columns: list[str],
) -> list[str]:
    baseline = next((item for item in candidate_reports if item["name"] == "dummy_mean_baseline"), None)
    summary = [
        f"Compared {len(candidate_reports)} candidate regressors on {rows} COMSOL sweep rows.",
        f"Inputs: {', '.join(input_columns)}; outputs: {', '.join(output_columns)}.",
        f"Selected {best['name']} with test RMSE {best['test_rmse']:.6g}, MAE {best['test_mae']:.6g}, R2 {best['test_r2']:.6g}.",
    ]
    if baseline and baseline["test_rmse"] > 0:
        improvement = 100.0 * (baseline["test_rmse"] - best["test_rmse"]) / baseline["test_rmse"]
        summary.append(f"Best model improved RMSE over mean baseline by {improvement:.1f}%.")
    return summary


def _recommendations(rows: int, best: dict[str, Any], warnings_list: list[str]) -> list[str]:
    recommendations = []
    if rows < 50:
        recommendations.append("Add more COMSOL parameter-sweep rows before relying on the surrogate for design decisions.")
    if best["test_r2"] < 0.8:
        recommendations.append("Inspect output nonlinearity and consider denser sweeps near sensitive parameter ranges.")
    if warnings_list:
        recommendations.append("Resolve data warnings, then retrain and compare the candidate reports again.")
    recommendations.append("Validate the saved surrogate on fresh COMSOL runs that were not included in the CSV.")
    recommendations.append("Keep the CSV, constraints JSON, generated script, and trained joblib together as one training record.")
    return _dedupe(recommendations)


def _dedupe(items: list[str]) -> list[str]:
    result = []
    seen = set()
    for item in items:
        if item and item not in seen:
            result.append(item)
            seen.add(item)
    return result
