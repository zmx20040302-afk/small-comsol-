from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {
    "model_name",
    "physics",
    "geometry",
    "materials",
    "boundary_conditions",
    "mesh",
    "study",
    "outputs",
}


class ConstraintError(ValueError):
    pass


def load_constraints(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_constraints(data)
    return data


def validate_constraints(data: dict[str, Any]) -> None:
    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        raise ConstraintError(f"Missing required sections: {', '.join(sorted(missing))}")

    if data["geometry"].get("type") != "rectangle_2d":
        raise ConstraintError("Only geometry.type='rectangle_2d' is supported by this starter template")

    if data["physics"] != "heat_transfer_solid":
        raise ConstraintError("Only physics='heat_transfer_solid' is supported by this starter template")

    for section_name in ("geometry", "materials", "boundary_conditions", "mesh"):
        section = data[section_name]
        parameters = section.get("parameters", section) if section_name == "geometry" else section
        if not isinstance(parameters, dict):
            raise ConstraintError(f"{section_name} must contain parameter dictionaries")
        for name, spec in parameters.items():
            _validate_numeric_spec(section_name, name, spec)

    if data["study"].get("type") not in {"stationary"}:
        raise ConstraintError("Only study.type='stationary' is supported by this starter template")

    if not data["outputs"]:
        raise ConstraintError("At least one output expression is required")


def _validate_numeric_spec(section_name: str, name: str, spec: dict[str, Any]) -> None:
    for key in ("value", "unit", "min", "max"):
        if key not in spec:
            raise ConstraintError(f"{section_name}.{name} is missing '{key}'")
    if float(spec["min"]) > float(spec["value"]) or float(spec["value"]) > float(spec["max"]):
        raise ConstraintError(
            f"{section_name}.{name} value={spec['value']} is outside [{spec['min']}, {spec['max']}]"
        )


def format_value(spec: dict[str, Any]) -> str:
    return f"{spec['value']}[{spec['unit']}]"
