from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .case_memory import generate_model_plan, query_memory


@dataclass(frozen=True)
class GeneratedComsolCode:
    requirement: str
    plan: dict[str, Any]
    matlab_code: str
    java_code: str
    theory_guidance: list[str]
    refinement_suggestions: list[str]
    existing_content_review: dict[str, Any]
    matlab_path: str
    java_path: str
    guidance_path: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "requirement": self.requirement,
            "plan": self.plan,
            "matlab_code": self.matlab_code,
            "java_code": self.java_code,
            "theory_guidance": self.theory_guidance,
            "refinement_suggestions": self.refinement_suggestions,
            "existing_content_review": self.existing_content_review,
            "outputs": {
                "matlab": self.matlab_path,
                "java": self.java_path,
                "guidance": self.guidance_path,
            },
        }


def generate_comsol_code_from_memory(
    requirement: str,
    memory_path: str | Path = "generated/case_memory/case_memory.json",
    output_dir: str | Path = "generated/code",
    output_prefix: str = "generated_comsol_model",
    top_k: int = 5,
    existing_content: str = "",
) -> GeneratedComsolCode:
    requirement = requirement.strip()
    if not requirement:
        raise ValueError("requirement is empty")

    plan = generate_model_plan(requirement, memory_path=memory_path, top_k=top_k)
    retrieval = query_memory(requirement, memory_path=memory_path, top_k=top_k)
    matched_cases = [item.get("case", {}) for item in retrieval.get("matches", [])]
    model_id = _safe_identifier(output_prefix or "generated_comsol_model")
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    matlab_path = destination / f"{model_id}.m"
    java_path = destination / f"{_java_class_name(model_id)}.java"
    guidance_path = destination / f"{model_id}_guidance.md"
    matlab_code = build_matlab_code(requirement, plan, model_id)
    java_code = build_java_code(requirement, plan, model_id)
    theory_guidance = build_theory_guidance(requirement, plan, matched_cases)
    existing_content_review = review_existing_content(existing_content, plan, matched_cases)
    refinement_suggestions = build_refinement_suggestions(existing_content_review, plan, matched_cases)
    matlab_path.write_text(matlab_code, encoding="utf-8")
    java_path.write_text(java_code, encoding="utf-8")
    guidance_path.write_text(
        build_guidance_markdown(
            requirement,
            plan,
            matched_cases,
            theory_guidance,
            refinement_suggestions,
            existing_content_review,
            matlab_path,
            java_path,
        ),
        encoding="utf-8",
    )
    return GeneratedComsolCode(
        requirement=requirement,
        plan=plan,
        matlab_code=matlab_code,
        java_code=java_code,
        theory_guidance=theory_guidance,
        refinement_suggestions=refinement_suggestions,
        existing_content_review=existing_content_review,
        matlab_path=str(matlab_path),
        java_path=str(java_path),
        guidance_path=str(guidance_path),
    )


def build_matlab_code(requirement: str, plan: dict[str, Any], model_id: str = "generated_comsol_model") -> str:
    function_name = _safe_identifier(f"build_{model_id}")
    lines = [
        f"function model = {function_name}()",
        f"%{function_name.upper()} Memory-assisted COMSOL LiveLink builder.",
        "% 由 comsol_training_small_model 生成。",
        f"% Requirement: {_comment_text(requirement)}",
        "% 正式运行前请复核几何尺寸、选择集和物理场特征名称。",
        "",
        "import com.comsol.model.*",
        "import com.comsol.model.util.*",
        "",
        "model = ModelUtil.create('Model');",
        f"model.label('{model_id}.mph');",
        "model.modelNode.create('mod1');",
        "",
        *_matlab_parameters(plan),
        "",
        "model.component.create('comp1', true);",
        f"model.component('comp1').geom.create('geom1', {_dimension(plan)});",
        "model.component('comp1').geom('geom1').lengthUnit('m');",
        "% TODO: 明确尺寸后，用已学习案例的几何序列替换这个起始几何。",
        *_matlab_geometry(plan),
        "",
        "model.component('comp1').material.create('mat1', 'Common');",
        "model.component('comp1').material('mat1').label('复核已学习案例中的材料');",
        "model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho_ref');",
        "model.component('comp1').material('mat1').propertyGroup('def').set('youngsmodulus', 'E_ref');",
        "model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', 'k_ref');",
        "",
        *_matlab_physics(plan),
        "",
        "model.component('comp1').mesh.create('mesh1');",
        "model.component('comp1').mesh('mesh1').create('size1', 'Size');",
        "model.component('comp1').mesh('mesh1').feature('size1').set('custom', true);",
        "model.component('comp1').mesh('mesh1').feature('size1').set('hmax', 'hmax');",
        "model.component('comp1').mesh('mesh1').run;",
        "",
        "model.study.create('std1');",
        "model.study('std1').create('stat', 'Stationary');",
        "model.study('std1').createAutoSequences('all');",
        "% model.study('std1').run; % Enable after boundary selections and loads are verified.",
        "",
        *_matlab_outputs(plan),
        "",
        "model.save(fullfile(pwd, [model.label]));",
        "end",
        "",
    ]
    return "\n".join(lines)


def build_java_code(requirement: str, plan: dict[str, Any], model_id: str = "generated_comsol_model") -> str:
    class_name = _java_class_name(model_id)
    lines = [
        "import com.comsol.model.*;",
        "import com.comsol.model.util.*;",
        "",
        f"public class {class_name} {{",
        "  public static Model run() {",
        "    Model model = ModelUtil.create(\"Model\");",
        f"    model.label(\"{model_id}.mph\");",
        "    model.modelNode().create(\"mod1\");",
        f"    // Requirement: {_comment_text(requirement)}",
        "    // 正式运行前请复核几何尺寸、选择集和物理场特征名称。",
        "",
        *_java_parameters(plan),
        "",
        "    model.component().create(\"comp1\", true);",
        f"    model.component(\"comp1\").geom().create(\"geom1\", {_dimension(plan)});",
        "    model.component(\"comp1\").geom(\"geom1\").lengthUnit(\"m\");",
        "    // TODO: 明确尺寸后，用已学习案例的几何序列替换这个起始几何。",
        *_java_geometry(plan),
        "",
        "    model.component(\"comp1\").material().create(\"mat1\", \"Common\");",
        "    model.component(\"comp1\").material(\"mat1\").label(\"复核已学习案例中的材料\");",
        "    model.component(\"comp1\").material(\"mat1\").propertyGroup(\"def\").set(\"density\", \"rho_ref\");",
        "    model.component(\"comp1\").material(\"mat1\").propertyGroup(\"def\").set(\"youngsmodulus\", \"E_ref\");",
        "    model.component(\"comp1\").material(\"mat1\").propertyGroup(\"def\").set(\"thermalconductivity\", \"k_ref\");",
        "",
        *_java_physics(plan),
        "",
        "    model.component(\"comp1\").mesh().create(\"mesh1\");",
        "    model.component(\"comp1\").mesh(\"mesh1\").create(\"size1\", \"Size\");",
        "    model.component(\"comp1\").mesh(\"mesh1\").feature(\"size1\").set(\"custom\", true);",
        "    model.component(\"comp1\").mesh(\"mesh1\").feature(\"size1\").set(\"hmax\", \"hmax\");",
        "    model.component(\"comp1\").mesh(\"mesh1\").run();",
        "",
        "    model.study().create(\"std1\");",
        "    model.study(\"std1\").create(\"stat\", \"Stationary\");",
        "    model.study(\"std1\").createAutoSequences(\"all\");",
        "    // model.study(\"std1\").run(); // Enable after boundary selections and loads are verified.",
        "",
        *_java_outputs(plan),
        "",
        "    return model;",
        "  }",
        "",
        "  public static void main(String[] args) {",
        "    Model model = run();",
        f"    model.save(\"{model_id}.mph\");",
        "  }",
        "}",
        "",
    ]
    return "\n".join(lines)


def build_theory_guidance(requirement: str, plan: dict[str, Any], matched_cases: list[dict[str, Any]]) -> list[str]:
    domains = set(plan.get("inferred_domains", []))
    content_physics = _merged_case_content(matched_cases, "physics")
    theory_keywords = _merged_case_content(matched_cases, "theory_keywords")
    guidance = [
        "建模顺序应保持为：参数 -> 几何 -> 选择集 -> 材料 -> 物理场 -> 边界/初始条件 -> 网格 -> 研究/求解 -> 结果导出。",
        "生成代码中的边界编号和选择集必须在 COMSOL 中复核；学习库只能提供案例模式和 API 结构，不能替代几何实体编号确认。",
    ]
    if "heat_transfer" in domains or any("HeatTransfer" in item for item in content_physics):
        guidance.append("传热模型需要确认热源、温度边界、热通量或对流换热条件，并检查材料的导热系数、密度和热容。")
    if "electromagnetics" in domains or any("ConductiveMedia" in item or "Electric" in item for item in content_physics):
        guidance.append("电流/电磁模型需要确认端子、电势、接地和绝缘边界；若与传热耦合，应把焦耳热或损耗项传递到热场。")
    if "fluid" in domains or any("LaminarFlow" in item for item in content_physics):
        guidance.append("流体模型需要确认入口、出口、壁面和压力条件；微流动案例通常还要同时检查稀物质传递或扩散系数。")
    if "structural" in domains or any("SolidMechanics" in item for item in content_physics):
        guidance.append("结构力学模型需要确认固定约束、载荷、接触/对称条件和材料弹性参数；特征频率问题应使用 Eigenfrequency 研究。")
    if "acoustics" in domains or any("PressureAcoustics" in item for item in content_physics):
        guidance.append("声学模型需要确认声硬边界、声源、压力条件和频域/特征频率研究设置。")
    if theory_keywords:
        guidance.append("已学习案例中的理论关键词包括：" + "，".join(theory_keywords[:12]) + "。")
    if matched_cases:
        names = "，".join(str(case.get("title", "案例")) for case in matched_cases[:5])
        guidance.append(f"本次生成优先参考以下已学习案例：{names}。")
    return guidance


def review_existing_content(existing_content: str, plan: dict[str, Any], matched_cases: list[dict[str, Any]]) -> dict[str, Any]:
    text = existing_content or ""
    lowered = text.lower()
    checks = {
        "has_parameters": "model.param" in lowered or ".param()" in lowered,
        "has_geometry": ".geom" in lowered,
        "has_physics": ".physics" in lowered,
        "has_material": ".material" in lowered,
        "has_mesh": ".mesh" in lowered,
        "has_study": ".study" in lowered,
        "has_results": ".result" in lowered,
        "has_boundary_selection": ".selection" in lowered,
    }
    expected_physics = [item["interface"] for item in _physics_specs(plan)]
    present_expected = [physics for physics in expected_physics if physics.lower() in lowered]
    missing_expected = [physics for physics in expected_physics if physics.lower() not in lowered]
    matched_content = {
        "physics": _merged_case_content(matched_cases, "physics")[:20],
        "geometry": _merged_case_content(matched_cases, "geometry")[:20],
        "studies": _merged_case_content(matched_cases, "studies")[:20],
        "results": _merged_case_content(matched_cases, "results")[:20],
    }
    return {
        "kind": "existing_comsol_content_review",
        "provided": bool(text.strip()),
        "length": len(text),
        "checks": checks,
        "expected_physics": expected_physics,
        "present_expected_physics": present_expected,
        "missing_expected_physics": missing_expected,
        "matched_case_content": matched_content,
    }


def build_refinement_suggestions(
    review: dict[str, Any],
    plan: dict[str, Any],
    matched_cases: list[dict[str, Any]],
) -> list[str]:
    suggestions = []
    if not review.get("provided"):
        suggestions.append("未提供现有脚本或模型摘要；本次输出为基于学习库的新建模型模板，可作为后续修正基线。")
    checks = review.get("checks", {})
    missing_steps = [
        ("has_parameters", "补充参数定义，并把关键尺寸、材料参数和载荷写成可扫描参数。"),
        ("has_geometry", "补充或替换几何构建段，优先复用相似案例中的几何序列。"),
        ("has_physics", "补充物理场接口，并与需求和已学习案例中的物理场保持一致。"),
        ("has_material", "补充材料节点，至少包含密度、弹性参数、导热或电学参数等必要属性。"),
        ("has_mesh", "补充网格设置，并在孔、裂纹、边界层或高梯度区域局部加密。"),
        ("has_study", "补充研究/求解器设置，按稳态、瞬态、频域、特征频率或参数扫描选择。"),
        ("has_results", "补充结果导出，保存关键全局量、场图和用于训练的 CSV。"),
        ("has_boundary_selection", "补充选择集或边界编号复核步骤，避免边界条件施加到错误实体。"),
    ]
    for key, message in missing_steps:
        if not checks.get(key, False):
            suggestions.append(message)
    for physics in review.get("missing_expected_physics", []):
        suggestions.append(f"根据需求和学习库，应补充或复核 `{physics}` 物理接口。")
    if matched_cases:
        best = matched_cases[0]
        content = best.get("case_content", {})
        if content.get("physics"):
            suggestions.append(f"可参考 `{best.get('title')}` 中的物理场设置：{', '.join(content.get('physics', [])[:5])}。")
        if content.get("studies"):
            suggestions.append(f"可参考 `{best.get('title')}` 中的研究设置：{', '.join(content.get('studies', [])[:5])}。")
    if not suggestions:
        suggestions.append("现有内容包含主要 COMSOL 建模段；下一步应在 COMSOL 中运行基准求解，并根据报错修正边界编号、材料属性和求解器设置。")
    return suggestions[:16]


def build_guidance_markdown(
    requirement: str,
    plan: dict[str, Any],
    matched_cases: list[dict[str, Any]],
    theory_guidance: list[str],
    refinement_suggestions: list[str],
    existing_content_review: dict[str, Any],
    matlab_path: Path,
    java_path: Path,
) -> str:
    lines = [
        "# COMSOL 建模代码与理论指导",
        "",
        f"- 需求: {requirement}",
        f"- MATLAB 输出: `{matlab_path}`",
        f"- Java 输出: `{java_path}`",
        "",
        "## 理论与建模指导",
        "",
    ]
    lines.extend(f"- {item}" for item in theory_guidance)
    lines.extend(["", "## 已学习案例证据", ""])
    for case in matched_cases[:8]:
        content = case.get("case_content", {})
        totals = content.get("totals", {})
        lines.append(
            f"- `{case.get('title', '案例')}`: 内容证据 {totals.get('model_tree_items', 0)} 条；"
            f"物理场={', '.join(content.get('physics', [])[:5]) or '未抽取'}"
        )
    lines.extend(["", "## 现有内容检查", ""])
    checks = existing_content_review.get("checks", {})
    if existing_content_review.get("provided"):
        for key, value in checks.items():
            lines.append(f"- {key}: {'已包含' if value else '缺失或未识别'}")
    else:
        lines.append("- 未提供现有内容，本次按新建模型模板处理。")
    lines.extend(["", "## 调整和完善建议", ""])
    lines.extend(f"- {item}" for item in refinement_suggestions)
    lines.extend(["", "## 后续验证路径", ""])
    lines.extend(
        [
            "- 在 COMSOL 中打开生成脚本，先不批量扫描，只运行一个基准模型。",
            "- 核对所有选择集、边界编号和材料参数。",
            "- 求解通过后，再添加参数扫描并导出 CSV。",
            "- 把修正后的 MATLAB/Java 脚本重新放回案例库，继续学习和完善记忆库。",
        ]
    )
    return "\n".join(lines) + "\n"


def _matlab_parameters(plan: dict[str, Any]) -> list[str]:
    lines = [
        "% Parameters merged from matched case memory and defaults.",
        "model.param.set('rho_ref', '2500[kg/m^3]', '默认密度；请替换为材料数据');",
        "model.param.set('E_ref', '35.1[GPa]', '默认杨氏模量；请替换为案例或文章数据');",
        "model.param.set('k_ref', '1[W/(m*K)]', '使用传热时的默认导热系数');",
        "model.param.set('hmax', '0.02[m]', 'Maximum mesh size');",
    ]
    for param in _safe_parameters(plan):
        lines.append(f"model.param.set('{param['name']}', '{_matlab_string(param['value'])}', '{_matlab_string(param['description'])}');")
    return lines


def _merged_case_content(matched_cases: list[dict[str, Any]], key: str) -> list[str]:
    values = []
    seen = set()
    for case in matched_cases:
        content = case.get("case_content", {}) if isinstance(case, dict) else {}
        for value in content.get(key, []):
            text = str(value).strip()
            if text and text not in seen:
                seen.add(text)
                values.append(text)
            if len(values) >= 80:
                return values
    return values


def _java_parameters(plan: dict[str, Any]) -> list[str]:
    lines = [
        "    // Parameters merged from matched case memory and defaults.",
        "    model.param().set(\"rho_ref\", \"2500[kg/m^3]\", \"默认密度；请替换为材料数据\");",
        "    model.param().set(\"E_ref\", \"35.1[GPa]\", \"默认杨氏模量；请替换为案例或文章数据\");",
        "    model.param().set(\"k_ref\", \"1[W/(m*K)]\", \"使用传热时的默认导热系数\");",
        "    model.param().set(\"hmax\", \"0.02[m]\", \"Maximum mesh size\");",
    ]
    for param in _safe_parameters(plan):
        lines.append(
            f"    model.param().set(\"{param['name']}\", \"{_java_string(param['value'])}\", \"{_java_string(param['description'])}\");"
        )
    return lines


def _matlab_geometry(plan: dict[str, Any]) -> list[str]:
    if _dimension(plan) == 3:
        return [
            "model.component('comp1').geom('geom1').create('blk1', 'Block');",
            "model.component('comp1').geom('geom1').feature('blk1').set('size', {'L_ref' 'W_ref' 'H_ref'});",
            "model.component('comp1').geom('geom1').run;",
        ]
    return [
        "model.component('comp1').geom('geom1').create('r1', 'Rectangle');",
        "model.component('comp1').geom('geom1').feature('r1').set('size', {'L_ref' 'W_ref'});",
        "model.component('comp1').geom('geom1').run;",
    ]


def _java_geometry(plan: dict[str, Any]) -> list[str]:
    if _dimension(plan) == 3:
        return [
            "    model.component(\"comp1\").geom(\"geom1\").create(\"blk1\", \"Block\");",
            "    model.component(\"comp1\").geom(\"geom1\").feature(\"blk1\").set(\"size\", new String[]{\"L_ref\", \"W_ref\", \"H_ref\"});",
            "    model.component(\"comp1\").geom(\"geom1\").run();",
        ]
    return [
        "    model.component(\"comp1\").geom(\"geom1\").create(\"r1\", \"Rectangle\");",
        "    model.component(\"comp1\").geom(\"geom1\").feature(\"r1\").set(\"size\", new String[]{\"L_ref\", \"W_ref\"});",
        "    model.component(\"comp1\").geom(\"geom1\").run();",
    ]


def _matlab_physics(plan: dict[str, Any]) -> list[str]:
    lines = ["% Physics inferred from requirement, matched cases, and COMSOL knowledge memory."]
    for spec in _physics_specs(plan):
        lines.extend(
            [
                f"model.component('comp1').physics.create('{spec['tag']}', '{spec['interface']}', 'geom1');",
                f"% {spec['note']}",
            ]
        )
    lines.append("% 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。")
    return lines


def _java_physics(plan: dict[str, Any]) -> list[str]:
    lines = ["    // Physics inferred from requirement, matched cases, and COMSOL knowledge memory."]
    for spec in _physics_specs(plan):
        lines.extend(
            [
                f"    model.component(\"comp1\").physics().create(\"{spec['tag']}\", \"{spec['interface']}\", \"geom1\");",
                f"    // {spec['note']}",
            ]
        )
    lines.append("    // 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。")
    return lines


def _matlab_outputs(plan: dict[str, Any]) -> list[str]:
    lines = ["% Derived values suggested by memory-assisted plan."]
    for index, output in enumerate(plan.get("candidate_outputs", [])[:8], start=1):
        tag = f"gev{index}"
        expr = _output_expression(str(output))
        lines.extend(
            [
                f"model.result.numerical.create('{tag}', 'EvalGlobal');",
                f"model.result.numerical('{tag}').label('{_matlab_string(str(output))}');",
                f"model.result.numerical('{tag}').set('expr', '{_matlab_string(expr)}');",
            ]
        )
    return lines


def _java_outputs(plan: dict[str, Any]) -> list[str]:
    lines = ["    // Derived values suggested by memory-assisted plan."]
    for index, output in enumerate(plan.get("candidate_outputs", [])[:8], start=1):
        tag = f"gev{index}"
        expr = _output_expression(str(output))
        lines.extend(
            [
                f"    model.result().numerical().create(\"{tag}\", \"EvalGlobal\");",
                f"    model.result().numerical(\"{tag}\").label(\"{_java_string(str(output))}\");",
                f"    model.result().numerical(\"{tag}\").set(\"expr\", \"{_java_string(expr)}\");",
            ]
        )
    return lines


def _physics_specs(plan: dict[str, Any]) -> list[dict[str, str]]:
    domains = set(plan.get("inferred_domains", []))
    for case in plan.get("matched_cases", []):
        domains.update(case.get("domains", []))
    specs = []
    if "heat_transfer" in domains:
        specs.append({"tag": "ht", "interface": "HeatTransferInSolids", "note": "Add heat flux, temperature, or convection features after selections are verified."})
    if "structural" in domains or "geomechanics" in domains:
        specs.append({"tag": "solid", "interface": "SolidMechanics", "note": "Add fixed constraints, loads, pore/fracture pressure, and stress boundary conditions."})
    if "fluid" in domains:
        specs.append({"tag": "spf", "interface": "LaminarFlow", "note": "Add inlet, outlet, wall, and pressure conditions; switch interface for porous/fracture flow if needed."})
    if "electromagnetics" in domains:
        specs.append({"tag": "ec", "interface": "ElectricCurrents", "note": "Add terminal, ground, and insulation boundary conditions."})
    if "acoustics" in domains:
        specs.append({"tag": "acpr", "interface": "PressureAcoustics", "note": "Add sound hard, pressure, source, or radiation boundaries."})
    return specs or [{"tag": "gph", "interface": "GeneralFormPDE", "note": "请替换为已学习案例所需的准确 COMSOL 物理接口。"}]


def _safe_parameters(plan: dict[str, Any]) -> list[dict[str, str]]:
    defaults = [
        {"name": "L_ref", "value": "1[m]", "description": "Reference length"},
        {"name": "W_ref", "value": "1[m]", "description": "Reference width"},
        {"name": "H_ref", "value": "0.1[m]", "description": "Reference height"},
    ]
    seen = {item["name"] for item in defaults}
    safe = list(defaults)
    for raw in plan.get("candidate_parameters", [])[:25]:
        name = _safe_param_name(str(raw.get("name", "")))
        if not name or name in seen:
            continue
        seen.add(name)
        safe.append(
            {
                "name": name,
                "value": str(raw.get("value") or "1"),
                "description": str(raw.get("description") or raw.get("source_case") or "已学习参数"),
            }
        )
    return safe


def _dimension(plan: dict[str, Any]) -> int:
    text = " ".join(
        [
            plan.get("requirement", ""),
            " ".join(plan.get("inferred_domains", [])),
            " ".join(case.get("title", "") for case in plan.get("matched_cases", [])),
        ]
    ).lower()
    return 3 if any(token in text for token in ("3d", "三维", "solid", "block", "volum", "空间")) else 2


def _output_expression(name: str) -> str:
    lowered = name.lower()
    if "temperature" in lowered or lowered in {"tmax", "tavg"}:
        return "T"
    if "stress" in lowered or "von" in lowered:
        return "solid.mises"
    if "displacement" in lowered:
        return "solid.disp"
    if "pressure" in lowered:
        return "p"
    if "velocity" in lowered or "flow" in lowered:
        return "spf.U"
    if "current" in lowered:
        return "ec.normJ"
    return "1"


def _safe_identifier(value: str) -> str:
    normalized = re.sub(r"\W+", "_", value, flags=re.ASCII).strip("_").lower()
    if not normalized or normalized[0].isdigit():
        normalized = f"model_{normalized or 'generated'}"
    return normalized[:80]


def _java_class_name(model_id: str) -> str:
    return "".join(part.capitalize() for part in _safe_identifier(model_id).split("_")) or "GeneratedComsolModel"


def _safe_param_name(value: str) -> str:
    name = re.sub(r"\W+", "_", value, flags=re.ASCII).strip("_")
    if not name:
        return ""
    if name[0].isdigit():
        name = f"p_{name}"
    return name[:40]


def _matlab_string(value: str) -> str:
    return value.replace("'", "''")


def _java_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _comment_text(value: str) -> str:
    return " ".join(value.split())[:500]
