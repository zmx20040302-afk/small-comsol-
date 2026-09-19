from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


def build_closure_audit(generated_dir: str | Path, program_path: str | Path) -> dict[str, Any]:
    """Summarize progress and evidence gaps without claiming engineering approval."""
    generated = Path(generated_dir)
    program = json.loads(Path(program_path).read_text(encoding="utf-8"))
    tasks = list(program.get("tasks", []))
    registry_paths = [generated / "models" / "surrogate_registry.json", generated / "surrogate_registry.json"]
    models_by_id: dict[str, dict[str, Any]] = {}
    for registry_path in registry_paths:
        if not registry_path.is_file():
            continue
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        for item in registry.get("models", []):
            if isinstance(item, dict):
                models_by_id[str(item.get("id", ""))] = item
    models = list(models_by_id.values())
    model_statuses = Counter(str(item.get("status", "unknown")) for item in models)
    lifecycle_statuses = Counter(str(item.get("lifecycle_status", "active")) for item in models)
    evidence_gaps: list[dict[str, str]] = []
    for item in models:
        for field in ("model_path", "model_card", "validation_report"):
            value = str(item.get(field, ""))
            if not value or not Path(value).is_file():
                evidence_gaps.append({"model_id": str(item.get("id", "unknown")), "missing": field})
    task_statuses = Counter(str(item.get("status", "unknown")) for item in tasks)
    ready_models = [
        item.get("id", "")
        for item in models
        if item.get("status") == "validated_for_declared_scope"
        and item.get("lifecycle_status", "active") == "active"
        and not any(gap["model_id"] == item.get("id", "") for gap in evidence_gaps)
    ]
    superseded_models = [
        {
            "id": str(item.get("id", "")),
            "superseded_by": str(item.get("superseded_by", "")),
            "reason": str(item.get("supersession_reason", "")),
        }
        for item in models
        if item.get("lifecycle_status") == "superseded"
    ]
    active_unvalidated_models = [
        str(item.get("id", ""))
        for item in models
        if item.get("status") != "validated_for_declared_scope"
        and item.get("lifecycle_status", "active") == "active"
    ]
    return {
        "kind": "comsol-training-closure-audit",
        "task_total": len(tasks),
        "task_statuses": dict(task_statuses),
        "registered_models": len(models),
        "model_statuses": dict(model_statuses),
        "model_lifecycle_statuses": dict(lifecycle_statuses),
        "ready_for_scoped_prediction": ready_models,
        "superseded_models": superseded_models,
        "active_unvalidated_models": active_unvalidated_models,
        "evidence_gaps": evidence_gaps,
        "guidance": "validated_for_declared_scope only permits rapid comparison inside the declared scope. It is not experimental or engineering certification.",
    }
