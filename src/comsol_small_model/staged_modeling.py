from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .boundary_knowledge import infer_boundary_conditions
from .case_memory import generate_model_plan
from .code_generator import generate_comsol_code_from_memory
from .coupled_physics_knowledge import analyze_coupled_physics
from .geometry_parameter_knowledge import analyze_geometry_parameters, validate_geometry_readiness
from .instruction_agent import _select_physics_from_requirement
from .material_property_knowledge import analyze_material_properties, validate_material_readiness
from .mesh_knowledge import infer_mesh_strategy
from .solver_knowledge import infer_study_solver
from .result_knowledge import infer_result_exports
from .modeling_readiness import assess_modeling_readiness


DEFAULT_WORKFLOW_DIR = Path("generated/staged_workflows")


STAGE_DEFINITIONS = [
    (
        "physics",
        "选择物理场",
        "Confirm physics interfaces, coupling assumptions, dependent variables, and boundary-condition families.",
    ),
    (
        "materials",
        "确定材料",
        "Confirm material groups, property sources, units, nonlinear/anisotropic assumptions, and parameterization.",
    ),
    (
        "data_structure",
        "建模数据与结构",
        "Confirm geometry source, dimensionality, selections, imported data, parameters, and data needed for training.",
    ),
    (
        "mesh",
        "网格策略",
        "Confirm global/local mesh size, boundary layers, refinement targets, and mesh-independence checks.",
    ),
    (
        "study_solver",
        "求解分步",
        "Confirm study sequence, stationary/transient/eigen/frequency/parametric settings, and solver risks.",
    ),
    (
        "results_export",
        "结果与导出",
        "Confirm derived values, plots, CSV export columns, validation criteria, and surrogate-training outputs.",
    ),
    (
        "final_generation",
        "完整模型生成",
        "Generate final COMSOL MATLAB/Java modeling plan after all previous steps are approved.",
    ),
]


def create_staged_workflow(
    requirement: str,
    memory_path: str | Path = "generated/case_memory/case_memory.json",
    output_dir: str | Path = DEFAULT_WORKFLOW_DIR,
    top_k: int = 5,
) -> dict[str, Any]:
    requirement = requirement.strip()
    if not requirement:
        raise ValueError("requirement is empty")
    plan = generate_model_plan(requirement, memory_path=memory_path, top_k=top_k)
    workflow_id = _workflow_id(requirement)
    workflow = {
        "kind": "comsol_staged_modeling_workflow",
        "workflow_id": workflow_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "requirement": requirement,
        "memory_path": str(memory_path),
        "status": "waiting_for_approval",
        "current_step": 0,
        "plan": plan,
        "steps": [_build_step(index, stage, plan, requirement) for index, stage in enumerate(STAGE_DEFINITIONS)],
        "approval_log": [],
    }
    outputs = save_workflow(workflow, output_dir)
    workflow["outputs"] = outputs
    return workflow


def approve_current_step(
    workflow_path: str | Path,
    approved: bool,
    comment: str = "",
    output_dir: str | Path | None = None,
) -> dict[str, Any]:
    workflow = load_workflow(workflow_path)
    step_index = int(workflow.get("current_step", 0))
    steps = workflow.get("steps", [])
    if step_index >= len(steps):
        workflow["status"] = "complete"
        return workflow

    step = steps[step_index]
    step["status"] = "approved" if approved else "needs_revision"
    step["approval"] = {
        "approved": approved,
        "comment": comment,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    workflow.setdefault("approval_log", []).append(
        {
            "step_id": step.get("id"),
            "approved": approved,
            "comment": comment,
            "timestamp": step["approval"]["timestamp"],
        }
    )
    if approved:
        workflow["current_step"] = min(step_index + 1, len(steps))
        workflow["status"] = "complete" if workflow["current_step"] >= len(steps) else "waiting_for_approval"
        if workflow["current_step"] < len(steps):
            steps[workflow["current_step"]]["status"] = "active"
    else:
        revision = _apply_step_revision(workflow, step, comment)
        step["status"] = "active"
        step["proposal"] = revision["proposal"]
        step["revision_guidance"] = revision["guidance"]
        step.setdefault("revision_history", []).append(revision["record"])
        workflow["status"] = "waiting_for_approval"
    workflow["updated_at"] = datetime.now(timezone.utc).isoformat()
    outputs = save_workflow(workflow, output_dir or Path(workflow_path).parent)
    workflow["outputs"] = outputs
    return workflow


def final_modeling_package(workflow_path: str | Path, output_dir: str | Path | None = None) -> dict[str, Any]:
    workflow = load_workflow(workflow_path)
    unapproved = [step for step in workflow.get("steps", [])[:-1] if step.get("status") != "approved"]
    if unapproved:
        raise ValueError("All modeling steps must be approved before final generation")
    destination = Path(output_dir or Path(workflow_path).parent)
    destination.mkdir(parents=True, exist_ok=True)
    approved_context = _approved_generation_context(workflow)
    generated = generate_comsol_code_from_memory(
        requirement=approved_context,
        memory_path=workflow.get("memory_path", "generated/case_memory/case_memory.json"),
        output_dir=destination / "final_code",
        output_prefix=str(workflow.get("workflow_id", "generated_comsol_model")),
        top_k=5,
        approved_domains=workflow.get("plan", {}).get("inferred_domains", []),
        approved_requirement=str(workflow.get("requirement", "")),
    )
    final_step = workflow.get("steps", [])[-1] if workflow.get("steps") else None
    if isinstance(final_step, dict):
        final_step["status"] = "approved"
        final_step["generated_outputs"] = generated.as_dict()["outputs"]
        final_step["approval"] = {
            "approved": True,
            "comment": "Final MATLAB and Java files generated from approved workflow decisions.",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    workflow["current_step"] = len(workflow.get("steps", []))
    workflow["status"] = "complete"
    workflow["updated_at"] = datetime.now(timezone.utc).isoformat()
    save_workflow(workflow, Path(workflow_path).parent)
    package = {
        "kind": "approved_comsol_modeling_package",
        "workflow_id": workflow.get("workflow_id"),
        "requirement": workflow.get("requirement"),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "approved_steps": workflow.get("steps", []),
        "approved_decisions": _approved_decisions(workflow),
        "modeling_sequence": _final_sequence(workflow),
        "matlab_generation_requirements": _matlab_requirements(workflow),
        "java_generation_requirements": _java_requirements(workflow),
        "verification_checklist": _verification_checklist(workflow),
        "material_readiness": validate_material_readiness(
            str(workflow.get("requirement", "")),
            workflow.get("plan", {}).get("inferred_domains", []),
            workflow.get("plan", {}).get("candidate_parameters", []),
        ),
        "modeling_readiness": assess_modeling_readiness(
            str(workflow.get("requirement", "")), workflow.get("plan", {})
        ),
        "generated_code": generated.as_dict(),
    }
    package["execution_handoff"] = _execution_handoff(package)
    _append_execution_handoff_to_guidance(
        Path(str(generated.guidance_path)),
        package["execution_handoff"],
        Path(str(generated.verification_path)),
        package["generated_code"].get("generation_readiness", {}).get("approved_domains", []),
    )
    json_path = destination / f"{workflow.get('workflow_id', 'workflow')}.final_modeling_package.json"
    md_path = destination / f"{workflow.get('workflow_id', 'workflow')}.final_modeling_package.md"
    json_path.write_text(json.dumps(package, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_package_markdown(package), encoding="utf-8")
    return {
        "package": package,
        "outputs": {
            "json": str(json_path),
            "markdown": str(md_path),
            **generated.as_dict()["outputs"],
        },
    }


def load_workflow(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_workflow(workflow: dict[str, Any], output_dir: str | Path = DEFAULT_WORKFLOW_DIR) -> dict[str, str]:
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    path = destination / f"{workflow.get('workflow_id', 'workflow')}.workflow.json"
    path.write_text(json.dumps(workflow, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"workflow": str(path)}


def _build_step(index: int, stage: tuple[str, str, str], plan: dict[str, Any], requirement: str) -> dict[str, Any]:
    step_id, title, purpose = stage
    status = "active" if index == 0 else "pending"
    return {
        "index": index,
        "id": step_id,
        "title": title,
        "purpose": purpose,
        "status": status,
        "proposal": _stage_proposal(step_id, plan, requirement),
        "evidence": _stage_evidence(step_id, plan),
        "approval_questions": _approval_questions(step_id),
        "approved_outputs": _approved_outputs(step_id),
    }


def _stage_proposal(step_id: str, plan: dict[str, Any], requirement: str) -> list[str]:
    domains = plan.get("inferred_domains", [])
    outputs = plan.get("candidate_outputs", [])
    parameters = [item.get("name", "") for item in plan.get("candidate_parameters", [])[:10]]
    matched = [item.get("title", "") for item in plan.get("matched_cases", [])[:5]]
    if step_id == "physics":
        selection = _select_physics_from_requirement(requirement, domains)
        boundary = infer_boundary_conditions(requirement, domains)
        coupling = analyze_coupled_physics(requirement, domains)
        return [
            "选择结果：" + selection["result"],
            "COMSOL 接口建议：" + selection["interfaces"],
            "理论依据：" + selection["theory"],
            "复合场检查：" + _coupling_summary(coupling),
            "边界条件判断：" + selection["boundaries"],
            "边界条件知识库：" + boundary["summary"] + " 建议边界类型：" + "、".join(boundary["boundary_types"][:6]) + "。",
            "初始条件建议：" + "、".join(boundary["initial_conditions"][:6]) + "。",
            "需要确认：" + selection["checks"],
            "相似案例参考：" + ", ".join(matched or ["暂无直接匹配案例"]) + "。",
        ]
    if step_id == "materials":
        material = analyze_material_properties(requirement, domains, plan.get("candidate_parameters", []))
        readiness = validate_material_readiness(requirement, domains, plan.get("candidate_parameters", []))
        recognized = material.get("recognized_materials", [])
        recognized_text = "; ".join(
            f"{item['name']}: " + ", ".join(f"{key}={value}" for key, value in item["properties"].items())
            for item in recognized
        )
        required = "；".join(
            f"{row['name']}({row['symbol']}, {row['unit']})" for row in material["required_properties"][:8]
        )
        optional = "；".join(
            f"{row['name']}({row['symbol']})" for row in material["optional_properties"][:6]
        )
        return [
            "材料与物性结论：" + material["summary"],
            "物性就绪检查：" + ("可以进入材料配置" if readiness["ready_for_model_generation"] else "暂不能进入最终求解模型，需先补充物性"),
            "物性联动风险：" + ("；".join(readiness["risks"]) or "未发现明显物性联动风险"),
            "默认物性假设：" + ("；".join(readiness["assumptions"]) or "未使用材料档案默认值"),
            "已识别材料配置：" + (recognized_text or "需求未明确材料名称，需要人工确认材料库条目。"),
            "必填物性参数：" + required,
            "可选/耦合物性：" + (optional or "暂无"),
            "温度/频率/方向依赖：" + "；".join(material["dependencies"][:5]),
            "待补充物性：" + ("、".join(row["name"] for row in material["missing_required_properties"][:8]) or "当前候选参数已覆盖主要必填项"),
            "MATLAB 材料设置应使用 material.propertyGroup('def').set(...)，并先用 model.param.set(...) 定义带单位参数。",
        ]
    if step_id == "data_structure":
        analysis = analyze_geometry_parameters(requirement, domains, plan.get("candidate_parameters", []))
        readiness = validate_geometry_readiness(requirement, domains, plan.get("candidate_parameters", []))
        parameter_text = ", ".join(
            f"{item['name']}={item['value']}" for item in analysis["parameters"][:8]
        )
        return [
            "几何与参数结论：" + analysis["summary"],
            "几何就绪检查：" + ("可以进入网格划分" if readiness["ready_for_meshing"] else "暂不能进入网格划分，需先补充几何证据"),
            "待补充几何信息：" + ("、".join(readiness["missing_geometry_evidence"]) or "当前几何证据基本完整"),
            "维度建议：" + analysis["dimension"],
            "几何要点：" + "；".join(analysis["geometry"][:6]),
            "关键参数：" + (parameter_text or ", ".join(parameters or ["需要人工补充尺寸、材料和载荷参数"])),
            "选择集建议：" + "；".join(analysis["selection_advice"][:6]),
            "后续扫描变量：" + "、".join(analysis["sweep_advice"][:6]),
        ]
    if step_id == "mesh":
        mesh = infer_mesh_strategy(requirement, domains)
        return [
            "网格策略：" + "；".join(mesh["strategy"]),
            "局部加密区域：" + ("、".join(mesh["local_refinements"]) or "需根据几何和结果梯度确认"),
            "网格参数：" + mesh["mesh_parameter"] + "，建议先做基准网格再做加密对比",
            "网格检查：" + "；".join(mesh["checks"]),
        ]
    if step_id == "study_solver":
        solver = infer_study_solver(requirement, domains)
        return [
            "研究类型：" + "、".join(solver["studies"]),
            "判断依据：" + "；".join(solver["reasons"]),
            "求解器检查：" + "；".join(solver["solver_checks"]),
            "案例库建议路径：" + ", ".join(plan.get("analysis_path", [])[:6]),
        ]
    if step_id == "results_export":
        result_plan = infer_result_exports(requirement, domains, outputs)
        return [
            "结果输出量：" + "、".join(result_plan["outputs"]),
            "导出格式：" + "、".join(result_plan["export_format"]),
            "结果校验：" + "；".join(result_plan["validation"]),
            "是否需要实验/现场对比：" + ("是" if result_plan["requires_reference_comparison"] else "暂未识别"),
        ]
    return [
        "Generate the complete COMSOL model only after all previous steps are approved.",
        "Final scripts should preserve comments for boundary IDs, selections, material data, and solver assumptions.",
    ]


def _coupling_summary(coupling: dict[str, Any]) -> str:
    if not coupling.get("is_coupled"):
        return str(coupling.get("summary", "暂未识别复合场。"))
    return (
        f"{coupling['summary']} 主物理场={coupling['primary_physics']}；"
        f"耦合物理场={'、'.join(coupling['coupled_physics'][:6])}；"
        f"多物理场节点={'、'.join(coupling['multiphysics_nodes'][:6])}；"
        f"耦合变量={'、'.join(coupling['coupling_variables'][:8])}。"
    )


def _stage_evidence(step_id: str, plan: dict[str, Any]) -> list[str]:
    evidence = [
        f"案例记忆数量：{plan.get('case_count', 0)}。",
        "匹配案例：" + ", ".join(item.get("title", "") for item in plan.get("matched_cases", [])[:5]),
    ]
    context = plan.get("knowledge_system_context", {})
    if context.get("available"):
        evidence.append("本地知识库已可用于相似案例检索、物理场判断、参数/输出量提取和建模步骤复用。")
    if step_id in {"physics", "study_solver", "results_export"}:
        evidence.extend(str(item) for item in plan.get("analysis_path", [])[:5])
    return [item for item in evidence if item]


def _approval_questions(step_id: str) -> list[str]:
    questions = {
        "physics": ["物理场是否正确？是否需要耦合其他物理场？", "边界条件类型是否已确认？"],
        "materials": ["材料属性和单位是否可靠？", "是否需要非线性、各向异性或温度相关材料？"],
        "data_structure": ["几何/数据结构是否符合建模对象？", "参数、选择集和导入数据是否完整？"],
        "mesh": ["网格尺度和局部加密区域是否合理？", "是否需要边界层或网格无关性检查？"],
        "study_solver": ["求解顺序是否合理？", "是否先做基准求解再做参数扫描？"],
        "results_export": ["输出量是否能验证模型？", "CSV 列是否满足后续训练需求？"],
        "final_generation": ["所有步骤是否已确认？", "是否可以生成完整 COMSOL MATLAB/Java 建模包？"],
    }
    return questions.get(step_id, ["该步骤是否正确？"])


def _approved_outputs(step_id: str) -> list[str]:
    return {
        "physics": ["approved_physics_interfaces", "approved_couplings", "boundary_condition_families"],
        "materials": ["approved_materials", "material_parameters", "unit_checks"],
        "data_structure": ["approved_geometry_or_data_structure", "named_selections", "input_parameters"],
        "mesh": ["approved_mesh_strategy", "refinement_targets", "mesh_validation_plan"],
        "study_solver": ["approved_study_sequence", "solver_settings", "parameter_sweep_plan"],
        "results_export": ["approved_outputs", "csv_export_columns", "validation_targets"],
        "final_generation": ["final_matlab_script", "final_java_script", "verification_report"],
    }.get(step_id, [])


def _revision_guidance(step: dict[str, Any], comment: str) -> list[str]:
    return [
        f"Revise step `{step.get('title', '')}` before continuing.",
        "User comment: " + (comment or "No comment provided."),
        "Update the proposal, then request approval again.",
    ]


def _apply_step_revision(
    workflow: dict[str, Any],
    step: dict[str, Any],
    comment: str,
) -> dict[str, Any]:
    clean_comment = " ".join(str(comment or "").split())
    if not clean_comment:
        clean_comment = "用户要求重新检查当前步骤，但尚未提供具体修改内容。"
    revised_requirement = (
        f"{workflow.get('requirement', '')}\n"
        f"用户对“{step.get('title', '')}”的修正意见（优先采用）：{clean_comment}"
    )
    regenerated = _stage_proposal(
        str(step.get("id", "")),
        workflow.get("plan", {}),
        revised_requirement,
    )
    proposal = [
        f"已应用本轮修正意见：{clean_comment}",
        *regenerated,
    ]
    timestamp = datetime.now(timezone.utc).isoformat()
    return {
        "proposal": proposal,
        "guidance": [
            "系统已根据用户意见重建当前步骤，请检查新方案后再次批准。",
            f"本轮修正：{clean_comment}",
        ],
        "record": {
            "comment": clean_comment,
            "timestamp": timestamp,
            "proposal": proposal,
        },
    }


def _approved_generation_context(workflow: dict[str, Any]) -> str:
    lines = [str(workflow.get("requirement", "")).strip(), "", "已批准建模决策："]
    for step in workflow.get("steps", [])[:-1]:
        if step.get("status") != "approved":
            continue
        lines.append(f"[{step.get('title', step.get('id', 'step'))}]")
        lines.extend(str(item) for item in step.get("proposal", [])[:12])
        comment = step.get("approval", {}).get("comment")
        if comment:
            lines.append("用户确认：" + str(comment))
    return "\n".join(item for item in lines if item is not None).strip()


def _approved_decisions(workflow: dict[str, Any]) -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    for step in workflow.get("steps", [])[:-1]:
        if step.get("status") != "approved":
            continue
        step_id = str(step.get("id", "step"))
        approval = step.get("approval", {})
        decisions[step_id] = {
            "title": step.get("title", step_id),
            "proposal": list(step.get("proposal", [])),
            "approved_outputs": list(step.get("approved_outputs", [])),
            "approval_comment": str(approval.get("comment", "")),
            "approved_at": approval.get("timestamp"),
        }
    return decisions


def _execution_handoff(package: dict[str, Any]) -> dict[str, Any]:
    readiness = package.get("generated_code", {}).get("generation_readiness", {})
    unresolved = list(readiness.get("unresolved_requirements", []))
    material = package.get("material_readiness", {})
    overall = package.get("modeling_readiness", {})
    material_ready = bool(material.get("ready_for_model_generation", False))
    if not material_ready:
        unresolved.extend(
            "缺少材料物性：" + str(row.get("name", "未命名物性"))
            for row in material.get("missing_required_properties", [])
        )
    for blocker in overall.get("blockers", []):
        if blocker not in unresolved:
            unresolved.append(str(blocker))
    unresolved = _dedupe_handoff_items(unresolved)
    solve_ready = bool(readiness.get("ready_to_solve", False)) and material_ready and bool(overall.get("ready_for_modeling", False))
    return {
        "kind": "comsol_execution_handoff",
        "workflow_id": package.get("workflow_id"),
        "approved_step_ids": list(package.get("approved_decisions", {}).keys()),
        "ready_to_open": bool(readiness.get("ready_to_open", False)),
        "ready_to_solve": solve_ready,
        "next_action": "start_baseline_solve" if solve_ready else (str(overall.get("next_action", "review_blockers")) if overall.get("blockers") else ("review_material_properties" if not material_ready else "review_named_selections_and_boundaries")),
        "unresolved_requirements": unresolved,
    }


def _append_execution_handoff_to_guidance(
    path: Path, handoff: dict[str, Any], verification_path: Path, approved_domains: list[str]
) -> None:
    """Keep the standalone guidance file aligned with the final package handoff."""
    next_action = str(handoff.get("next_action", "review_blockers"))
    unresolved = list(handoff.get("unresolved_requirements", []))
    lines = [
        "",
        "## 执行前确认",
        "",
        f"- 可打开模型：`{handoff.get('ready_to_open', False)}`",
        f"- 可直接求解：`{handoff.get('ready_to_solve', False)}`",
        f"- 下一步：`{next_action}`",
        f"- 操作说明：{_handoff_action_guidance(next_action)}",
        f"- 待核对项数量：`{len(unresolved)}`",
        f"- 完成条件：{_handoff_completion_guidance(handoff, unresolved)}",
        f"- 验证记录：`{verification_path}`",
        f"- 实际采用物理场：{_domain_labels(approved_domains)}",
    ]
    if unresolved:
        lines.append(f"- 优先处理：{unresolved[0]}")
    for item in unresolved:
        lines.append(f"- 求解前核对：{item}")
    path.write_text(path.read_text(encoding="utf-8") + "\n".join(lines) + "\n", encoding="utf-8")


def _domain_labels(domains: list[str]) -> str:
    labels = {
        "heat_transfer": "传热",
        "electromagnetics": "电流/电磁",
        "structural": "结构力学",
        "geomechanics": "岩土力学",
        "fluid": "流体流动",
        "electrochemistry": "电化学",
        "acoustics": "声学",
        "optimization": "优化",
        "geometry": "几何",
    }
    return " + ".join(labels.get(str(domain), str(domain)) for domain in domains) or "待确认"


def _handoff_action_guidance(action: str) -> str:
    guidance = {
        "start_baseline_solve": "在 COMSOL 中先运行一个基准工况，再检查求解日志和结果是否合理。",
        "review_named_selections_and_boundaries": "在 COMSOL 中核对端子、接地、对流面等命名选择集及其边界条件，然后再运行基准工况。",
        "review_material_properties": "补充或确认材料物性、单位及其温度或频率依赖关系，再运行基准工况。",
        "review_blockers": "逐项处理下方列出的未解决条件，完成后再生成或求解模型。",
    }
    return guidance.get(action, "根据下方未解决项完成核对后，再运行基准工况。")


def _handoff_completion_guidance(handoff: dict[str, Any], unresolved: list[str]) -> str:
    if handoff.get("ready_to_solve", False):
        return "当前模型已通过生成阶段检查，可执行一个基准工况求解并检查结果。"
    if unresolved:
        return "逐项完成下方核对内容，并重新生成最终模型包；确认可直接求解后再运行基准工况。"
    return "在 COMSOL 中复核当前设置后，重新生成最终模型包以确认求解状态。"


def _dedupe_handoff_items(items: list[str]) -> list[str]:
    """Remove repeated material variants while preserving the first explanation."""
    result: list[str] = []
    material_names: set[str] = set()
    for raw in items:
        item = str(raw)
        if item.startswith("补充材料物性：") or item.startswith("材料：") or item.startswith("缺少材料物性："):
            name = item.split("：", 1)[1].strip()
            if name in material_names:
                continue
            material_names.add(name)
        if item not in result:
            result.append(item)
    return result


def _final_sequence(workflow: dict[str, Any]) -> list[str]:
    return [
        "Define parameters and units.",
        "Build/import geometry and selections.",
        "Assign materials.",
        "Create approved physics interfaces and boundary conditions.",
        "Create mesh and refinement settings.",
        "Create study and solver sequence.",
        "Export approved results and CSV training columns.",
        "Save model and report verification checklist.",
    ]


def _matlab_requirements(workflow: dict[str, Any]) -> list[str]:
    requirements = [
        "Use LiveLink MATLAB API in the approved sequence.",
        "Keep boundary IDs and named selections as explicit review comments.",
        "Add table export for approved outputs.",
        f"Requirement: {workflow.get('requirement', '')}",
    ]
    requirement = str(workflow.get("requirement", "")).lower()
    if any(token in requirement for token in ("不同电压", "比较不同", "参数扫描", "sweep", "parametric", "compare different", "different voltage")):
        requirements.append("Voltage sweep uses the review-only default range 0.1-1 mV with 37 sample points; replace it with approved values before solving.")
    return requirements


def _java_requirements(workflow: dict[str, Any]) -> list[str]:
    return [
        "Use COMSOL Java API equivalents for parameters, geometry, physics, mesh, study, and results.",
        "Keep comments where COMSOL entity IDs must be verified.",
        "Save the final model as MPH after baseline solve settings are reviewed.",
    ]


def _verification_checklist(workflow: dict[str, Any]) -> list[str]:
    checklist = [
        "Confirm material units and property sources.",
        "Confirm boundary selections after geometry generation.",
        "Run one baseline solve before parameter sweeps.",
        "Run mesh refinement checks for key outputs.",
        "Export CSV only after derived values are verified.",
    ]
    readiness = validate_material_readiness(
        str(workflow.get("requirement", "")),
        workflow.get("plan", {}).get("inferred_domains", []),
        workflow.get("plan", {}).get("candidate_parameters", []),
    )
    if not readiness["ready_for_model_generation"]:
        checklist.insert(1, "补充材料物性后再进行最终求解；当前缺少：" + "、".join(row["name"] for row in readiness["missing_required_properties"]))
    return checklist


def _package_markdown(package: dict[str, Any]) -> str:
    lines = [
        "# Approved COMSOL Modeling Package",
        "",
        f"- Workflow: `{package.get('workflow_id', '')}`",
        f"- Requirement: {package.get('requirement', '')}",
        "",
        "## Modeling Sequence",
        "",
    ]
    lines.extend(f"- {item}" for item in package.get("modeling_sequence", []))
    lines.extend(["", "## MATLAB Requirements", ""])
    lines.extend(f"- {item}" for item in package.get("matlab_generation_requirements", []))
    lines.extend(["", "## Java Requirements", ""])
    lines.extend(f"- {item}" for item in package.get("java_generation_requirements", []))
    lines.extend(["", "## Verification Checklist", ""])
    lines.extend(f"- {item}" for item in package.get("verification_checklist", []))
    material = package.get("material_readiness", {})
    lines.extend(["", "## Material Readiness", ""])
    lines.append(f"- ready_for_model_generation: `{material.get('ready_for_model_generation', False)}`")
    for item in material.get("risks", []):
        lines.append(f"- risk: {item}")
    overall = package.get("modeling_readiness", {})
    lines.extend(["", "## Overall Modeling Readiness", ""])
    lines.append(f"- ready_for_modeling: `{overall.get('ready_for_modeling', False)}`")
    lines.append(f"- next_action: `{overall.get('next_action', 'review_blockers')}`")
    for item in overall.get("blockers", []):
        lines.append(f"- blocker: {item}")
    generated = package.get("generated_code", {})
    outputs = generated.get("outputs", {}) if isinstance(generated, dict) else {}
    readiness = generated.get("generation_readiness", {}) if isinstance(generated, dict) else {}
    handoff = package.get("execution_handoff", {})
    lines.extend(["", "## Generated Files", ""])
    for name, path in outputs.items():
        lines.append(f"- {name}: `{path}`")
    lines.extend(["", "## Generation Readiness", ""])
    lines.append(f"- status: `{readiness.get('status', 'unknown')}`")
    lines.append(f"- ready_to_open: `{handoff.get('ready_to_open', readiness.get('ready_to_open', False))}`")
    lines.append(f"- ready_to_solve: `{handoff.get('ready_to_solve', False)}`")
    for item in readiness.get("unresolved_requirements", []):
        lines.append(f"- unresolved: {item}")
    lines.extend(["", "## Execution Handoff", ""])
    lines.append(f"- next_action: `{handoff.get('next_action', 'unknown')}`")
    lines.append(f"- approved_steps: `{', '.join(handoff.get('approved_step_ids', []))}`")
    for item in handoff.get("unresolved_requirements", []):
        lines.append(f"- review_before_execution: {item}")
    return "\n".join(lines) + "\n"


def _workflow_id(requirement: str) -> str:
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "_", requirement.strip(), flags=re.UNICODE).strip("_")
    slug = slug[:40] or "comsol_workflow"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    return f"{slug}_{stamp}"
