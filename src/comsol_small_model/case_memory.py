from __future__ import annotations

import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .knowledge_bridge import enrich_plan_with_external_knowledge


DEFAULT_MEMORY_PATH = Path("generated/case_memory/case_memory.json")


DOMAIN_KEYWORDS = {
    "geometry": [
        "geometry",
        "geom",
        "part",
        "assembly",
        "selection",
        "extrude",
        "workplane",
        "busbar",
        "snowflake",
        "koch",
        "fractal",
        "几何",
        "装配",
        "科赫",
        "雪花",
        "分形",
    ],
    "heat_transfer": ["heat", "temperature", "thermal", "tmax", "tavg", "传热", "温度", "热"],
    "structural": ["stress", "strain", "displacement", "solid", "mechanics", "结构", "应力", "位移"],
    "electromagnetics": ["electric", "current", "voltage", "magnetic", "acdc", "电流", "电压", "电磁"],
    "fluid": ["flow", "velocity", "pressure", "cfd", "fluid", "流体", "压力", "速度"],
    "electrochemistry": ["electrochem", "corrosion", "battery", "electrode", "电化学", "腐蚀", "电池"],
    "acoustics": ["acoustic", "pressure acoustics", "eigenfrequency", "声学", "声压"],
    "optimization": ["optimization", "objective", "constraint", "优化", "目标函数"],
}


def remember_case(card: dict[str, Any], memory_path: str | Path = DEFAULT_MEMORY_PATH) -> dict[str, Any]:
    memory = load_memory(memory_path)
    entry = _memory_entry(card)
    cases = [
        item
        for item in memory["cases"]
        if item.get("case_dir") != entry["case_dir"] and item.get("title") != entry["title"]
    ]
    cases.append(entry)
    memory["cases"] = sorted(cases, key=lambda item: item["title"])
    memory["updated_at"] = datetime.now(timezone.utc).isoformat()
    _write_memory(memory_path, memory)
    return {"memory_path": str(memory_path), "entry": entry, "case_count": len(memory["cases"])}


def load_memory(memory_path: str | Path = DEFAULT_MEMORY_PATH) -> dict[str, Any]:
    path = Path(memory_path)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "kind": "comsol_case_memory",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "cases": [],
    }


def query_memory(query: str, memory_path: str | Path = DEFAULT_MEMORY_PATH, top_k: int = 5) -> dict[str, Any]:
    memory = load_memory(memory_path)
    query_tokens = _tokens(query)
    scored = []
    for entry in memory.get("cases", []):
        score = _score(query_tokens, entry)
        if score > 0:
            scored.append({"score": score, "case": entry})
    scored.sort(key=lambda item: item["score"], reverse=True)
    return {
        "kind": "case_memory_query",
        "query": query,
        "top_k": top_k,
        "matches": scored[:top_k],
        "case_count": len(memory.get("cases", [])),
    }


def generate_model_plan(requirement: str, memory_path: str | Path = DEFAULT_MEMORY_PATH, top_k: int = 5) -> dict[str, Any]:
    retrieval = query_memory(requirement, memory_path=memory_path, top_k=top_k)
    domains = _infer_domains(requirement)
    matched_cases = [item["case"] for item in retrieval["matches"]]
    parameters = _merge_parameters(matched_cases)
    outputs = _suggest_outputs(requirement, domains)
    plan = {
        "kind": "comsol_model_plan",
        "requirement": requirement,
        "inferred_domains": domains,
        "case_count": retrieval["case_count"],
        "matched_cases": [
            {
                "title": item["case"]["title"],
                "score": item["score"],
                "training_stage": item["case"].get("training_stage"),
                "domains": item["case"].get("domains", []),
            }
            for item in retrieval["matches"]
        ],
        "recommended_modeling_steps": _modeling_steps(domains, bool(matched_cases)),
        "candidate_parameters": parameters[:30],
        "candidate_outputs": outputs,
        "analysis_path": _analysis_path(domains),
        "training_path": [
            "根据选定参数和范围创建或改写约束 JSON。",
            "结合已校验约束和相似案例证据生成 LiveLink MATLAB 建模脚本。",
            "运行 COMSOL 参数扫描并生成 CSV 数据。",
            "使用选定输入列和输出列训练本地代理模型。",
            "用未参与训练的 COMSOL 结果验证 RMSE、MAE、R2 和测试预测。",
        ],
        "limitations": _plan_limitations(retrieval["case_count"], matched_cases),
    }
    return enrich_plan_with_external_knowledge(plan, requirement)


def _memory_entry(card: dict[str, Any]) -> dict[str, Any]:
    case_content = card.get("case_content", {}) if isinstance(card.get("case_content"), dict) else {}
    text_parts = [
        card.get("title", ""),
        card.get("case_dir", ""),
        card.get("training_stage", ""),
        card.get("post_learning_summary", {}).get("summary", ""),
        " ".join(card.get("thoughts", [])),
        " ".join(card.get("implementation_path", [])),
        " ".join(card.get("gaps", [])),
        " ".join(case_content.get("parameters", [])),
        " ".join(case_content.get("geometry", [])),
        " ".join(case_content.get("physics", [])),
        " ".join(case_content.get("materials", [])),
        " ".join(case_content.get("mesh", [])),
        " ".join(case_content.get("studies", [])),
        " ".join(case_content.get("results", [])),
        " ".join(case_content.get("boundary_conditions", [])),
        " ".join(case_content.get("theory_keywords", [])),
    ]
    for source in case_content.get("source_extracts", []):
        if isinstance(source, dict):
            text_parts.extend(
                [
                    source.get("name", ""),
                    " ".join(source.get("content_summary", [])),
                    " ".join(source.get("physics", [])),
                    " ".join(source.get("geometry", [])),
                ]
            )
    for param in card.get("parameters", []):
        text_parts.extend([param.get("name", ""), param.get("description", ""), param.get("value", "")])
    for source in card.get("source_files", []):
        text_parts.extend([source.get("name", ""), source.get("kind", "")])
    text = " ".join(text_parts)
    return {
        "title": card.get("title", "case"),
        "case_dir": card.get("case_dir", ""),
        "training_stage": card.get("training_stage", "unknown"),
        "updated_at": card.get("created_at", datetime.now(timezone.utc).isoformat()),
        "file_summary": card.get("file_summary", {}),
        "parameters": card.get("parameters", [])[:80],
        "case_content": _memory_case_content(case_content),
        "post_learning_summary": card.get("post_learning_summary", {}),
        "knowledge_alignment": card.get("knowledge_alignment", {}),
        "thoughts": card.get("thoughts", []),
        "implementation_path": card.get("implementation_path", []),
        "gaps": card.get("gaps", []),
        "domains": _infer_domains(text),
        "keywords": sorted(_tokens(text))[:300],
        "search_text": text,
    }


def _memory_case_content(case_content: dict[str, Any]) -> dict[str, Any]:
    if not case_content:
        return {}
    return {
        "totals": case_content.get("totals", {}),
        "parameters": case_content.get("parameters", [])[:40],
        "geometry": case_content.get("geometry", [])[:40],
        "physics": case_content.get("physics", [])[:40],
        "materials": case_content.get("materials", [])[:30],
        "mesh": case_content.get("mesh", [])[:30],
        "studies": case_content.get("studies", [])[:30],
        "results": case_content.get("results", [])[:30],
        "boundary_conditions": case_content.get("boundary_conditions", [])[:30],
        "theory_keywords": case_content.get("theory_keywords", [])[:30],
    }


def _write_memory(memory_path: str | Path, memory: dict[str, Any]) -> None:
    path = Path(memory_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(memory, ensure_ascii=False, indent=2), encoding="utf-8")


def _tokens(text: str) -> set[str]:
    tokens = {token.lower() for token in re.findall(r"[A-Za-z0-9_]+", text) if len(token) > 1}
    for run in re.findall(r"[\u4e00-\u9fff]+", text):
        if len(run) > 1:
            tokens.add(run)
        tokens.update(run[index : index + 2] for index in range(max(0, len(run) - 1)))
        tokens.update(run[index : index + 3] for index in range(max(0, len(run) - 2)))
    return tokens


def _score(query_tokens: set[str], entry: dict[str, Any]) -> float:
    if not query_tokens:
        return 0.0
    case_tokens = set(entry.get("keywords", [])) | _tokens(entry.get("search_text", ""))
    overlap = query_tokens & case_tokens
    title = str(entry.get("title", ""))
    title_tokens = _tokens(title)
    title_overlap = query_tokens & title_tokens
    query_text = "".join(sorted(query_tokens, key=len, reverse=True))
    title_bonus = 0.0
    if title and title in query_text:
        title_bonus += 5.0
    title_bonus += len(title_overlap) * 2.5
    domain_bonus = len(set(entry.get("domains", [])) & set(_infer_domains(" ".join(query_tokens)))) * 2.0
    parameter_bonus = sum(1 for param in entry.get("parameters", []) if param.get("name", "").lower() in query_tokens) * 1.5
    return len(overlap) / math.sqrt(max(len(case_tokens), 1)) + title_bonus + domain_bonus + parameter_bonus


def _infer_domains(text: str) -> list[str]:
    lowered = text.lower()
    domains = []
    for domain, words in DOMAIN_KEYWORDS.items():
        if any(word.lower() in lowered for word in words):
            domains.append(domain)
    return domains or ["general_multiphysics"]


def _merge_parameters(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for case in cases:
        for param in case.get("parameters", []):
            name = param.get("name")
            if name and name not in merged:
                merged[name] = {
                    "name": name,
                    "value": param.get("value", ""),
                    "description": param.get("description", ""),
                    "source_case": case.get("title", ""),
                }
    return list(merged.values())


def _suggest_outputs(requirement: str, domains: list[str]) -> list[str]:
    lowered = requirement.lower()
    outputs = []
    if "geometry" in domains:
        outputs.extend(["volume_total", "surface_area_total", "entity_count", "geometry_build_success"])
    if "heat_transfer" in domains or "temperature" in lowered:
        outputs.extend(["Tmax", "Tavg", "heat_flux_integral"])
    if "structural" in domains:
        outputs.extend(["max_displacement", "max_von_mises_stress", "reaction_force"])
    if "electromagnetics" in domains:
        outputs.extend(["max_current_density", "electric_resistance", "terminal_current"])
    if "fluid" in domains:
        outputs.extend(["pressure_drop", "max_velocity", "flow_rate"])
    return outputs or ["primary_quantity_of_interest", "validation_error"]


def _modeling_steps(domains: list[str], has_cases: bool) -> list[str]:
    steps = [
        "Clarify model objective, dimensionality, input parameters, outputs, and validation targets.",
        "Choose geometry strategy: reuse similar case script, import CAD, or generate parametric geometry.",
        "Define materials, units, selections, and reusable parameter groups.",
        "Add physics interfaces and boundary/initial conditions.",
        "Create mesh and study sequence, then solve a baseline model.",
        "Export derived values and plots for validation.",
    ]
    if has_cases:
        steps.insert(1, "查看检索到的相似案例，并复用其参数命名、几何序列和 LiveLink API 调用模式。")
    if "optimization" in domains:
        steps.append("Add objective, constraints, and optimization study after the baseline model is verified.")
    return steps


def _analysis_path(domains: list[str]) -> list[str]:
    path = ["Baseline solve", "Mesh refinement check", "Parameter sweep", "Result validation"]
    if "heat_transfer" in domains:
        path.append("Temperature and heat-flux sensitivity analysis")
    if "structural" in domains:
        path.append("Stress/displacement safety check")
    if "electromagnetics" in domains:
        path.append("Current/field distribution and loss analysis")
    if "fluid" in domains:
        path.append("Pressure drop and flow uniformity analysis")
    path.append("Surrogate training dataset export")
    return path


def _plan_limitations(case_count: int, matched_cases: list[dict[str, Any]]) -> list[str]:
    limitations = []
    if case_count < 5:
        limitations.append("Case memory is still small; generated plans should be reviewed carefully.")
    if not matched_cases:
        limitations.append("No similar case was found; plan relies on general COMSOL modeling logic.")
    if matched_cases and all(case.get("training_stage") != "ready_for_surrogate_training" for case in matched_cases):
        limitations.append("Retrieved cases mainly support modeling logic; numerical training still needs CSV sweep data.")
    return limitations or ["No major limitation detected from current memory."]
