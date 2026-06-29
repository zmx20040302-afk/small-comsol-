from __future__ import annotations

from typing import Any


def respond_to_instruction(
    instruction: str,
    file_summary: dict[str, Any] | None = None,
    model_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    text = instruction.strip()
    lowered = text.lower()
    intents: list[str] = []
    feedback: list[str] = []
    next_actions: list[str] = []

    if not text:
        return {
            "intent": ["empty"],
            "feedback": ["请先输入建模、文件阅读、训练或约束相关需求。"],
            "next_actions": [],
            "assistant_message": "请先输入一个和 COMSOL 案例学习、建模、约束、仿真或代理模型训练有关的问题。",
            "explanation_sections": [],
            "suggested_tool": "chat",
        }

    if _contains_any(lowered, ["读取", "阅读", "解析", "文件", "read", "inspect", "file"]):
        intents.append("read_file")
        feedback.append("我可以先读取文件摘要；MATLAB .m 文件通常能暴露参数、物理场、研究和结果设置。")
        next_actions.append("先使用文件阅读功能，再检查提取出的摘要。")

    if _contains_any(lowered, ["学习", "总结", "归纳", "案例", "summary", "summarize", "learn", "pdf", "java"]):
        intents.append("learning_summary")
        feedback.append("我可以把相关 COMSOL PDF、MATLAB 建模脚本、Java 导出、MPH 文件、JSON 元数据和 CSV 数据汇总成一个学习包。")
        next_actions.append("把相关文件一起读取，然后生成学习总结。")

    if _contains_any(lowered, ["建模", "生成", "自动", "模型", "comsol", "livelink", "build", "generate", "model"]):
        intents.append("generate_comsol_model")
        feedback.append("我可以根据已校验的约束 JSON 或案例记忆生成 COMSOL LiveLink MATLAB/Java 建模脚本。")
        next_actions.append("先校验约束或检索案例记忆，再生成建模脚本。")

    if _contains_any(lowered, ["约束", "限制", "范围", "边界", "条件", "constraint", "limit"]):
        intents.append("validate_constraints")
        feedback.append("约束应包含几何、材料、边界条件、网格、研究类型和输出量。")
        next_actions.append("检查所有数值是否处在允许范围内。")

    if _contains_any(lowered, ["训练", "代理", "预测", "csv", "train", "surrogate", "predict"]):
        intents.append("train_surrogate")
        feedback.append("代理模型训练需要 COMSOL 参数扫描 CSV，并明确输入列和输出列。")
        next_actions.append("确认依赖已安装，然后用选定的 CSV 列训练。")

    if _contains_any(lowered, [".mph", "mph"]):
        intents.append("read_mph")
        feedback.append(".mph 文件应通过 COMSOL with MATLAB 导出摘要；仅靠 Python 不能可靠恢复完整模型树。")
        next_actions.append("在 COMSOL with MATLAB 中运行 matlab/export_mph_summary.m。")

    if file_summary:
        feedback.append(_feedback_for_file_kind(str(file_summary.get("kind", "unknown")), file_summary))

    if not intents:
        intents.append("general")
        feedback.append("我可以帮助你在文件阅读、脚本生成、约束校验和代理模型训练之间选择下一步。")
        next_actions.append("添加一个或多个文件，或说明要读取、生成、校验还是训练。")

    return {
        "intent": intents,
        "feedback": feedback,
        "next_actions": next_actions,
        "assistant_message": _assistant_message(text, intents, feedback, next_actions, file_summary, model_plan),
        "explanation_sections": _explanation_sections(intents, file_summary, model_plan),
        "suggested_tool": _suggested_tool(intents),
    }


def _contains_any(text: str, needles: list[str]) -> bool:
    return any(needle.lower() in text for needle in needles)


def _feedback_for_file_kind(kind: str, file_summary: dict[str, Any]) -> str:
    name = file_summary.get("name", "file")
    details = file_summary.get("details", {})
    if kind == "matlab_livelink":
        return (
            f"已识别 {name} 为 COMSOL MATLAB LiveLink 脚本，包含 "
            f"{details.get('parameters', 0)} 个参数，可作为自动建模模板来源。"
        )
    if kind == "csv_table":
        columns = details.get("columns", [])
        return f"已识别 {name} 为可用于代理模型训练的 CSV 表格，列包括：{', '.join(columns[:12])}。"
    if kind == "json":
        return f"已识别 {name} 为 JSON，可能是约束配置或导出的模型摘要。"
    if kind == "comsol_mph":
        return f"已识别 {name} 为 .mph 文件，需要先通过 COMSOL LiveLink 导出摘要。"
    if kind == "file_collection":
        return (
            f"Read {details.get('count', 0)} files: "
            f"{details.get('matlab_files', 0)} MATLAB, "
            f"{details.get('java_files', 0)} Java, "
            f"{details.get('pdf_files', 0)} PDF, "
            f"{details.get('csv_files', 0)} CSV, "
            f"{details.get('json_files', 0)} JSON, "
            f"{details.get('mph_files', 0)} MPH. "
            "我可以把这些文件合并判断建模模板、约束条件和训练数据。"
        )
    return f"已读取 {name}，可根据预览判断它是否支持建模或训练。"


def _assistant_message(
    instruction: str,
    intents: list[str],
    feedback: list[str],
    next_actions: list[str],
    file_summary: dict[str, Any] | None,
    model_plan: dict[str, Any] | None,
) -> str:
    lines = [
        f"我会把这个问题当作 COMSOL 训练任务来处理：{instruction}",
        "",
        "我的理解：你希望把案例、文件或约束转化为可复用的建模知识，而不是只做一次性的文件读取。",
    ]
    if "read_file" in intents:
        lines.append("第一步要先读文件证据：MATLAB/Java 用来恢复模型树，PDF 用来理解理论和建模目的，MPH 用来回到 COMSOL 侧验证真实设置。")
    if "learning_summary" in intents:
        lines.append("学习后的总结会沉淀为案例卡，记录建模逻辑、参数、可复用脚本、训练就绪状态和后续缺口。")
    if "generate_comsol_model" in intents:
        lines.append("建模时我会按 COMSOL 底层顺序组织：参数、几何、选择集、材料、物理场、网格、研究、结果导出。")
    if "validate_constraints" in intents:
        lines.append("约束部分会重点检查参数范围、边界条件、单位、输出量和是否能转成 LiveLink MATLAB 脚本。")
    if "train_surrogate" in intents:
        lines.append("训练小模型需要参数扫描 CSV；案例脚本本身先用于学习建模逻辑，数值代理模型要等 sweep 数据存在后再训练。")
    if file_summary:
        lines.append("")
        lines.append("当前文件上下文：" + _compact_file_context(file_summary))
    if model_plan:
        matches = model_plan.get("matched_cases", [])
        lines.append("")
        if matches:
            names = ", ".join(str(item.get("title", "case")) for item in matches[:3])
            lines.append(f"我在本地案例记忆中找到相似案例：{names}。可以优先复用这些案例的参数命名、几何顺序和 API 调用模式。")
        else:
            lines.append("本地案例记忆暂时没有强匹配案例，因此会先按通用 COMSOL 建模流程给方案。")
    if feedback:
        lines.append("")
        lines.append("判断依据：" + " ".join(feedback[:3]))
    if next_actions:
        lines.append("")
        lines.append("下一步我建议：" + " -> ".join(next_actions[:4]))
    return "\n".join(lines)


def _explanation_sections(
    intents: list[str],
    file_summary: dict[str, Any] | None,
    model_plan: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = [
        {
            "title": "COMSOL 训练对话逻辑",
            "items": [
                "先理解需求属于文件阅读、案例学习、约束校验、建模生成还是代理模型训练。",
                "再把可执行证据和理论证据分开：脚本负责模型树，PDF 负责理论，CSV 负责训练。",
                "最后给出可操作的下一步，而不是只返回分类结果。",
            ],
        }
    ]
    if file_summary:
        sections.append({"title": "已读文件如何使用", "items": [_compact_file_context(file_summary)]})
    if model_plan:
        sections.append(
            {
                "title": "记忆库辅助",
                "items": [
                    f"当前记忆库案例数：{model_plan.get('case_count', 0)}",
                    "匹配案例可作为参数、几何顺序和训练路径的参考。",
                ],
            }
        )
    if "train_surrogate" in intents:
        sections.append(
            {
                "title": "训练判断",
                "items": [
                    "没有 CSV 时不能直接训练数值代理模型。",
                    "有 MATLAB/Java/MPH/PDF 时，可以先学习建模逻辑，再用 COMSOL 参数扫描生成训练数据。",
                ],
            }
        )
    return sections


def _suggested_tool(intents: list[str]) -> str:
    if "read_file" in intents:
        return "read_files"
    if "learning_summary" in intents:
        return "learning_summary"
    if "validate_constraints" in intents:
        return "validate_constraints"
    if "generate_comsol_model" in intents:
        return "plan_or_generate_model"
    if "train_surrogate" in intents:
        return "train_surrogate"
    return "chat"


def _compact_file_context(file_summary: dict[str, Any]) -> str:
    kind = str(file_summary.get("kind", "unknown"))
    details = file_summary.get("details", {})
    if kind == "file_collection":
        return (
            f"已读 {details.get('count', 0)} 个文件，其中 MATLAB={details.get('matlab_files', 0)}, "
            f"Java={details.get('java_files', 0)}, PDF={details.get('pdf_files', 0)}, "
            f"MPH={details.get('mph_files', 0)}, CSV={details.get('csv_files', 0)}。"
        )
    return f"已读 {file_summary.get('name', 'file')}，类型为 {kind}。"
