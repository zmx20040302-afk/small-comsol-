from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Any


def validate_constraint_results(config: dict[str, Any], csv_path: str | Path) -> dict[str, Any]:
    """Check outputs from the small verified templates against boundary data."""
    values = _read_values(csv_path)
    checks: list[dict[str, Any]] = []
    physics = str(config.get("physics", ""))
    boundary = dict(config.get("boundary_conditions", {}))

    if physics == "heat_transfer_1d":
        left, right = _value(boundary, "T_left"), _value(boundary, "T_right")
        checks.append(_range_check("T_max", values, min(left, right), max(left, right), "最大温度应位于两个定温边界之间。"))
    elif physics == "diffusion_1d":
        expected = max(_value(boundary, "c_left"), _value(boundary, "c_right"))
        actual = values.get("c_max")
        checks.append({"name": "concentration_boundary_match", "passed": actual is not None and math.isclose(actual, expected, rel_tol=1e-5, abs_tol=1e-9), "actual": actual, "expected": expected, "reason": "稳态无反应扩散的最大浓度应等于较高定浓度边界。"})
    elif physics == "electrothermal_1d":
        ambient = max(_value(boundary, "T_left"), _value(boundary, "T_right"))
        temperature, joule = values.get("T_max"), values.get("Q_joule_max")
        checks.extend([
            {"name": "joule_temperature_rise", "passed": temperature is not None and temperature > ambient, "actual": temperature, "expected": f"> {ambient}", "reason": "正焦耳热下内部最高温度应高于定温边界。"},
            {"name": "positive_joule_heat", "passed": joule is not None and joule > 0, "actual": joule, "expected": "> 0", "reason": "通电导体的焦耳热密度应为正。"},
        ])
    elif physics == "solid_mechanics_2d":
        displacement, stress = values.get("u_max"), values.get("mises_max")
        checks.extend([
            {"name": "positive_displacement", "passed": displacement is not None and displacement > 0, "actual": displacement, "expected": "> 0", "reason": "受载且存在固定约束时，应出现有限的非零位移。"},
            {"name": "positive_von_mises_stress", "passed": stress is not None and stress > 0, "actual": stress, "expected": "> 0", "reason": "受载固体应出现正的等效应力。"},
        ])
    elif physics == "thermal_stress_2d":
        hot, cold = _value(boundary, "T_hot"), _value(boundary, "T_cold")
        temperature, displacement, stress = values.get("T_max"), values.get("u_max"), values.get("mises_max")
        checks.extend([
            _range_check("T_max", values, min(hot, cold), max(hot, cold), "最高温度应位于冷热定温边界之间。"),
            {"name": "thermal_displacement", "passed": displacement is not None and displacement > 0, "actual": displacement, "expected": "> 0", "reason": "存在温差、热膨胀系数和约束时，应出现非零位移。"},
            {"name": "thermal_von_mises_stress", "passed": stress is not None and stress > 0, "actual": stress, "expected": "> 0", "reason": "受约束热膨胀应产生正的等效应力。"},
        ])
    elif physics == "axial_bar_1d":
        displacement, stress = values.get("u_max"), values.get("mises_max")
        checks.extend([
            {"name": "axial_bar_displacement", "passed": displacement is not None and displacement > 0, "actual": displacement, "expected": "> 0", "reason": "固定一端并在另一端施加正轴向面力时，杆件应产生有限正位移。"},
            {"name": "axial_bar_stress", "passed": stress is not None and stress > 0, "actual": stress, "expected": "> 0", "reason": "受轴向面力的线弹性杆件应产生正的等效应力。"},
        ])

    passed = bool(checks) and all(bool(check["passed"]) for check in checks)
    return {"kind": "constraint_result_validation", "physics": physics, "values": values, "checks": checks, "passed": passed, "summary": "物理结果检查通过。" if passed else "结果文件存在，但物理结果检查未通过或尚无规则。"}


def _read_values(csv_path: str | Path) -> dict[str, float]:
    with Path(csv_path).open("r", encoding="utf-8", newline="") as handle:
        result = {str(row["name"]): float(str(row["value"])) for row in csv.DictReader(handle) if str(row.get("name", "")).strip()}
    if not result or not all(math.isfinite(value) for value in result.values()):
        raise ValueError("results CSV has no finite numeric outputs")
    return result


def _value(section: dict[str, Any], name: str) -> float:
    value = section[name]
    return float(value["value"]) if isinstance(value, dict) else float(value)


def _range_check(name: str, values: dict[str, float], lower: float, upper: float, reason: str) -> dict[str, Any]:
    actual = values.get(name)
    tolerance = max(1e-8, abs(upper - lower) * 1e-5)
    return {"name": f"{name}_range", "passed": actual is not None and lower - tolerance <= actual <= upper + tolerance, "actual": actual, "expected": [lower, upper], "reason": reason}
