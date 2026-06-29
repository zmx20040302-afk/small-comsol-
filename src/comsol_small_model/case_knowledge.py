from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .file_reader import build_learning_summary, summarize_files
from .knowledge_bridge import compare_with_external_knowledge


SUPPORTED_CASE_EXTENSIONS = {".pdf", ".m", ".java", ".mph", ".txt", ".json", ".csv", ".md"}
RESERVED_PARAMETER_NAMES = {
    "class",
    "def",
    "else",
    "for",
    "from",
    "function",
    "if",
    "import",
    "package",
    "public",
    "return",
    "static",
    "while",
}


def summarize_case_directory(
    case_dir: str | Path,
    title: str | None = None,
    output_dir: str | Path = "generated/case_knowledge",
) -> dict[str, Any]:
    case_path = Path(case_dir)
    if not case_path.exists() or not case_path.is_dir():
        raise FileNotFoundError(f"Case directory not found: {case_path}")

    files = _case_files(case_path)
    if not files:
        raise ValueError(f"No supported COMSOL case files found in {case_path}")

    collection = summarize_files(files)
    learning = build_learning_summary(collection)
    card = build_case_card(case_path, collection, learning, title=title)
    outputs = write_case_card(card, output_dir)
    return {"card": card, "outputs": outputs}


def build_case_card(
    case_path: Path,
    collection: dict[str, Any],
    learning: dict[str, Any],
    title: str | None = None,
) -> dict[str, Any]:
    details = collection.get("details", {})
    parameters = _extract_parameters(collection)
    case_content = _extract_case_content(collection)
    has_training_csv = details.get("csv_files", 0) > 0
    has_model_scripts = details.get("matlab_files", 0) > 0 or details.get("java_files", 0) > 0
    has_pdf = details.get("pdf_files", 0) > 0
    has_mph = details.get("mph_files", 0) > 0

    training_stage = "ready_for_surrogate_training" if has_training_csv else "needs_comsol_sweep_csv"
    if has_model_scripts and not has_training_csv:
        training_stage = "modeling_logic_learning_ready"

    thoughts = []
    if has_pdf:
        thoughts.append("PDF 文档用于理解案例目的、建模顺序、理论假设和验证目标。")
    if has_model_scripts:
        thoughts.append("MATLAB 和 Java 文件是 COMSOL 模型树的可执行证据，应驱动自动建模脚本生成。")
    if has_mph:
        thoughts.append("MPH 文件需要通过 COMSOL with MATLAB 导出摘要后，才能可靠使用内部模型设置。")
    if parameters:
        thoughts.append("参数文本和脚本证据可转换为约束和参数扫描变量。")
    if case_content["totals"]["model_tree_items"] > 0:
        thoughts.append("已从案例内容中抽取到模型树证据，可用于学习几何、物理场、材料、网格、研究和结果设置。")
    if not has_training_csv:
        thoughts.append("未发现训练 CSV，因此数值代理模型训练前需要先导出 COMSOL 参数扫描数据。")
    else:
        thoughts.append("已发现 CSV 数据，可先检查输入/输出列再训练。")

    card = {
        "kind": "comsol_case_card",
        "title": title or case_path.name,
        "case_dir": str(case_path),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "training_stage": training_stage,
        "file_summary": {
            "count": details.get("count", 0),
            "kinds": details.get("kinds", {}),
            "matlab_files": details.get("matlab_files", 0),
            "java_files": details.get("java_files", 0),
            "pdf_files": details.get("pdf_files", 0),
            "mph_files": details.get("mph_files", 0),
            "csv_files": details.get("csv_files", 0),
            "json_files": details.get("json_files", 0),
        },
        "parameters": parameters,
        "case_content": case_content,
        "learning_summary": learning,
        "thoughts": thoughts,
        "implementation_path": _implementation_path(has_training_csv),
        "gaps": _gaps(has_training_csv, has_mph, parameters),
        "source_files": [
            {
                "name": file.get("name"),
                "kind": file.get("kind"),
                "size_bytes": file.get("size_bytes"),
                "details": file.get("details", {}),
            }
            for file in collection.get("files", [])
        ],
    }
    card["post_learning_summary"] = _post_learning_summary(card)
    card["knowledge_alignment"] = compare_with_external_knowledge(card)
    return card


def write_case_card(card: dict[str, Any], output_dir: str | Path) -> dict[str, str]:
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    slug = _slugify(str(card["title"]))
    json_path = destination / f"{slug}.case.json"
    md_path = destination / f"{slug}.case.md"
    index_path = destination / "case_knowledge_index.json"

    json_path.write_text(json.dumps(card, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(case_card_markdown(card), encoding="utf-8")
    _upsert_index(index_path, card, json_path, md_path)
    return {"json": str(json_path), "markdown": str(md_path), "index": str(index_path)}


def case_card_markdown(card: dict[str, Any]) -> str:
    lines = [
        f"# {card['title']}",
        "",
        f"- Case directory: `{card['case_dir']}`",
        f"- Training stage: `{card['training_stage']}`",
        f"- Created at: `{card['created_at']}`",
        "",
        "## File Summary",
        "",
    ]
    for key, value in card["file_summary"].items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Extracted Parameters", ""])
    if card["parameters"]:
        for param in card["parameters"][:80]:
            lines.append(
                f"- `{param['name']}` = `{param['value']}`"
                + (f" - {param['description']}" if param.get("description") else "")
            )
    else:
        lines.append("- No explicit parameter table was detected.")

    content = card.get("case_content", {})
    totals = content.get("totals", {})
    lines.extend(["", "## 内容级读取结果", ""])
    lines.append(f"- 模型树证据数量: {totals.get('model_tree_items', 0)}")
    lines.append(f"- 理论关键词: {', '.join(content.get('theory_keywords', [])) or '未自动识别'}")
    for section in ("geometry", "physics", "materials", "mesh", "studies", "results", "boundary_conditions"):
        values = content.get(section, [])
        if values:
            lines.append(f"- {section}: {', '.join(values[:12])}")
    source_extracts = content.get("source_extracts", [])
    if source_extracts:
        lines.extend(["", "### 文件内容证据", ""])
        for item in source_extracts[:20]:
            lines.append(
                f"- `{item.get('name', '')}`: "
                f"参数={len(item.get('parameters', []))}, "
                f"几何={len(item.get('geometry', []))}, "
                f"物理场={len(item.get('physics', []))}, "
                f"研究={len(item.get('studies', []))}, "
                f"结果={len(item.get('results', []))}"
            )

    lines.extend(["", "## Thoughts", ""])
    for thought in card["thoughts"]:
        lines.append(f"- {thought}")

    summary = card.get("post_learning_summary", {})
    if summary:
        lines.extend(["", "## Learning Summary After This Case", ""])
        lines.append(f"- Summary: {summary.get('summary', '')}")
        lines.append(f"- Training readiness: {summary.get('training_readiness', '')}")
        lines.append(f"- Reusable confidence: {summary.get('reusable_confidence', '')}")
        lines.extend(["", "### 学到的建模逻辑", ""])
        for item in summary.get("learned_modeling_logic", []):
            lines.append(f"- {item}")
        lines.extend(["", "### Reusable Assets", ""])
        for item in summary.get("reusable_assets", []):
            lines.append(f"- {item}")
        lines.extend(["", "### Learning Process and Evidence", ""])
        for item in summary.get("learning_trace", []):
            lines.append(f"- **{item.get('step', '')}**")
            lines.append(f"  - Evidence: {item.get('evidence', '')}")
            lines.append(f"  - Judgement: {item.get('judgement', '')}")
        lines.extend(["", "### Next Actions", ""])
        for item in summary.get("next_actions", []):
            lines.append(f"- {item}")

    alignment = card.get("knowledge_alignment", {})
    if alignment:
        lines.extend(["", "## External Knowledge Alignment", ""])
        lines.extend(["", "### Similar Master Cases", ""])
        matches = alignment.get("case_matches", [])
        if matches:
            for match in matches[:5]:
                fields = ", ".join(match.get("supported_fields", [])) or "topic only"
                lines.append(
                    f"- `{match.get('title', '')}` score={match.get('score', '')}; "
                    f"fields={fields}; parameters={match.get('parameter_count', 0)}"
                )
        else:
            lines.append("- No master case index match was available.")
        lines.extend(["", "### Official Documentation Checks", ""])
        docs = alignment.get("docs_matches", [])
        if docs:
            for doc in docs[:5]:
                lines.append(
                    f"- `{doc.get('document', '')}` page {doc.get('page', '')}; "
                    f"module={doc.get('module', '')}; score={doc.get('score', '')}"
                )
        else:
            lines.append("- No official documentation index match was available.")
        lines.extend(["", "### Training Improvements", ""])
        for item in alignment.get("training_improvements", []):
            lines.append(f"- {item}")

    lines.extend(["", "## Implementation Path", ""])
    for step in card["implementation_path"]:
        lines.append(f"- {step}")

    lines.extend(["", "## Gaps", ""])
    for gap in card["gaps"]:
        lines.append(f"- {gap}")

    lines.extend(["", "## Source Files", ""])
    for file in card["source_files"]:
        lines.append(f"- `{file['name']}` ({file['kind']}, {file['size_bytes']} bytes)")
    lines.append("")
    return "\n".join(lines)


def _case_files(case_path: Path) -> list[Path]:
    return sorted(
        [
            path
            for path in case_path.rglob("*")
            if path.is_file() and path.suffix.lower() in SUPPORTED_CASE_EXTENSIONS
        ]
    )


def _extract_parameters(collection: dict[str, Any]) -> list[dict[str, str]]:
    parameters: dict[str, dict[str, str]] = {}
    for file in collection.get("files", []):
        if file.get("kind") not in {"text", "matlab_livelink", "matlab_text", "comsol_java"}:
            continue
        preview = str(file.get("preview", ""))
        for param in _extract_parameter_lines(preview):
            parameters.setdefault(param["name"], param)
    return list(parameters.values())


def _extract_case_content(collection: dict[str, Any]) -> dict[str, Any]:
    sections = {
        "parameters": [],
        "geometry": [],
        "physics": [],
        "materials": [],
        "mesh": [],
        "studies": [],
        "results": [],
        "boundary_conditions": [],
        "theory_keywords": [],
    }
    source_extracts = []
    for file in collection.get("files", []):
        details = file.get("details", {}) if isinstance(file, dict) else {}
        extract = details.get("content_extract", {}) if isinstance(details, dict) else {}
        if not isinstance(extract, dict):
            continue
        source_item = {
            "name": file.get("name", "file"),
            "kind": file.get("kind", "unknown"),
            "evidence_score": extract.get("evidence_score", 0),
            "content_summary": extract.get("content_summary", [])[:8],
        }
        for key in sections:
            values = [str(value) for value in extract.get(key, []) if str(value).strip()]
            source_item[key] = values[:20]
            sections[key].extend(values)
        source_extracts.append(source_item)

    deduped = {key: _dedupe(values, limit=80) for key, values in sections.items()}
    model_tree_items = sum(
        len(deduped[key])
        for key in ("parameters", "geometry", "physics", "materials", "mesh", "studies", "results", "boundary_conditions")
    )
    return {
        "kind": "case_content_learning",
        **deduped,
        "source_extracts": sorted(source_extracts, key=lambda item: item.get("evidence_score", 0), reverse=True),
        "totals": {
            "model_tree_items": model_tree_items,
            "source_files_with_content": sum(1 for item in source_extracts if item.get("evidence_score", 0) > 0),
            "source_files_checked": len(source_extracts),
        },
    }


def _dedupe(values: list[str], limit: int = 80) -> list[str]:
    result = []
    seen = set()
    for value in values:
        normalized = re.sub(r"\s+", " ", value.strip())
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
        if len(result) >= limit:
            break
    return result


def _extract_parameter_lines(text: str) -> list[dict[str, str]]:
    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("%") or stripped.startswith("//"):
            continue
        if stripped.endswith(";"):
            matlab_match = re.search(
                r"model\.param\.set\(\s*'(?P<name>[^']+)'\s*,\s*'(?P<value>[^']+)'(?:\s*,\s*'(?P<description>[^']*)')?",
                stripped,
            )
            if matlab_match:
                rows.append(
                    {
                        "name": matlab_match.group("name"),
                        "value": matlab_match.group("value"),
                        "description": matlab_match.group("description") or "",
                        "source": "matlab_param_set",
                    }
                )
                continue
            matlab_input_match = re.search(
                r"inputParam\.set\(\s*'(?P<name>[^']+)'\s*,\s*'(?P<value>[^']+)'",
                stripped,
            )
            if matlab_input_match:
                rows.append(
                    {
                        "name": matlab_input_match.group("name"),
                        "value": matlab_input_match.group("value"),
                        "description": "geometry input parameter",
                        "source": "matlab_geometry_input_param",
                    }
                )
                continue
            java_match = re.search(
                r"\.param\(\)\.set\(\s*\"(?P<name>[^\"]+)\"\s*,\s*\"(?P<value>[^\"]+)\"(?:\s*,\s*\"(?P<description>[^\"]*)\")?",
                stripped,
            )
            if java_match:
                rows.append(
                    {
                        "name": java_match.group("name"),
                        "value": java_match.group("value"),
                        "description": java_match.group("description") or "",
                        "source": "java_param_set",
                    }
                )
                continue
            java_input_match = re.search(
                r"inputParam\(\)\.set\(\s*\"(?P<name>[^\"]+)\"\s*,\s*\"(?P<value>[^\"]+)\"",
                stripped,
            )
            if java_input_match:
                rows.append(
                    {
                        "name": java_input_match.group("name"),
                        "value": java_input_match.group("value"),
                        "description": "geometry input parameter",
                        "source": "java_geometry_input_param",
                    }
                )
            continue
        table_match = re.match(r"^(?P<name>[A-Za-z]\w*)\s+(?P<value>[^\s]+(?:\[[^\]]+\])?)\s*(?P<desc>\".*\")?$", stripped)
        if table_match and _is_valid_parameter_name(table_match.group("name")):
            rows.append(
                {
                    "name": table_match.group("name"),
                    "value": table_match.group("value"),
                    "description": (table_match.group("desc") or "").strip('"'),
                    "source": "parameter_table",
                }
            )
            continue
    return rows


def _is_valid_parameter_name(name: str) -> bool:
    return name.lower() not in RESERVED_PARAMETER_NAMES


def _implementation_path(has_training_csv: bool) -> list[str]:
    steps = [
        "把 PDF、MATLAB、Java、MPH、TXT、JSON 和 CSV 证据作为一个完整案例包读取。",
        "Extract model purpose, geometry sequence, parameters, selections, and model-tree features.",
        "Convert detected parameters into a constraints JSON with units and valid ranges.",
        "Use MATLAB/Java evidence to generate or adapt a LiveLink MATLAB builder.",
    ]
    if has_training_csv:
        steps.extend(
            [
                "Inspect CSV columns and choose surrogate inputs and outputs.",
                "Train the local surrogate model and review RMSE, MAE, R2, and warnings.",
            ]
        )
    else:
        steps.extend(
            [
                "Run a COMSOL parametric sweep over selected parameters.",
                "Export a CSV containing input parameters and target outputs.",
                "Train the local surrogate model after the CSV exists.",
            ]
        )
    return steps


def _post_learning_summary(card: dict[str, Any]) -> dict[str, Any]:
    file_summary = card.get("file_summary", {})
    parameters = card.get("parameters", [])
    case_content = card.get("case_content", {})
    content_totals = case_content.get("totals", {})
    has_scripts = file_summary.get("matlab_files", 0) > 0 or file_summary.get("java_files", 0) > 0
    has_pdf = file_summary.get("pdf_files", 0) > 0
    has_mph = file_summary.get("mph_files", 0) > 0
    has_csv = file_summary.get("csv_files", 0) > 0

    learned_logic = [
        "Case files were treated as one COMSOL evidence package: documentation, scripts, binary model files, parameters, and data.",
        "The model tree should be reconstructed in this order: parameters, geometry, selections, materials, physics, mesh, study, results, and exports.",
    ]
    if has_scripts:
        learned_logic.append("MATLAB/Java scripts provide reusable COMSOL API call patterns for automated model construction.")
    if has_pdf:
        learned_logic.append("PDF documentation provides modeling purpose, assumptions, theoretical context, and validation targets.")
    if has_mph:
        learned_logic.append("MPH files are remembered as authoritative model artifacts, but detailed internal settings require COMSOL/LiveLink extraction.")
    if parameters:
        learned_logic.append("检测到的参数可用于生成约束 JSON，后续也可作为代理模型训练的扫描变量。")
    if content_totals.get("model_tree_items", 0):
        learned_logic.append(
            "已完成内容级读取：从案例文件中抽取了参数、几何、物理场、材料、网格、研究、结果和边界条件等模型树证据。"
        )

    reusable_assets = []
    if parameters:
        reusable_assets.append(f"{len(parameters)} extracted parameters with values/descriptions.")
    if has_scripts:
        reusable_assets.append("LiveLink MATLAB or COMSOL Java script structure.")
    if has_pdf:
        reusable_assets.append("Theory and workflow evidence from PDF documents.")
    if has_mph:
        reusable_assets.append("Original MPH files for later COMSOL-side verification.")
    if has_csv:
        reusable_assets.append("CSV data for direct surrogate training.")
    if content_totals.get("model_tree_items", 0):
        reusable_assets.append(f"{content_totals.get('model_tree_items', 0)} 条内容级模型树证据。")

    next_actions = list(card.get("implementation_path", []))
    if not has_csv:
        next_actions.append("几何和建模逻辑验证后，运行 COMSOL 参数扫描并导出 CSV 训练数据。")

    return {
        "kind": "post_case_learning_summary",
        "title": card.get("title", "case"),
        "summary": (
            f"已学习 {card.get('title', 'case')} 的 {file_summary.get('count', 0)} 个文件；"
            f"训练阶段={card.get('training_stage', 'unknown')}；参数数量={len(parameters)}；"
            f"内容证据={content_totals.get('model_tree_items', 0)} 条。"
        ),
        "learned_modeling_logic": learned_logic,
        "reusable_assets": reusable_assets or ["No reusable asset was detected automatically."],
        "training_readiness": (
            "ready_for_surrogate_training"
            if has_csv
            else "modeling_logic_ready_but_needs_comsol_sweep_csv"
        ),
        "reusable_confidence": _reusable_confidence(has_scripts, has_pdf, has_mph, parameters, has_csv),
        "learning_trace": _learning_trace(card),
        "next_actions": next_actions,
    }


def _learning_trace(card: dict[str, Any]) -> list[dict[str, str]]:
    file_summary = card.get("file_summary", {})
    parameters = card.get("parameters", [])
    case_content = card.get("case_content", {})
    content_totals = case_content.get("totals", {})
    source_files = card.get("source_files", [])
    has_scripts = file_summary.get("matlab_files", 0) > 0 or file_summary.get("java_files", 0) > 0
    has_pdf = file_summary.get("pdf_files", 0) > 0
    has_mph = file_summary.get("mph_files", 0) > 0
    has_csv = file_summary.get("csv_files", 0) > 0
    script_names = [
        str(file.get("name"))
        for file in source_files
        if file.get("kind") in {"matlab_livelink", "matlab_text", "comsol_java"}
    ][:6]

    trace = [
        {
            "step": "1. 文件证据读取",
            "evidence": (
                f"共读取 {file_summary.get('count', 0)} 个案例文件；"
                f"MATLAB={file_summary.get('matlab_files', 0)}，"
                f"Java={file_summary.get('java_files', 0)}，"
                f"PDF={file_summary.get('pdf_files', 0)}，"
                f"MPH={file_summary.get('mph_files', 0)}，"
                f"CSV={file_summary.get('csv_files', 0)}。"
            ),
            "judgement": "这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。",
        },
        {
            "step": "2. 内容级模型树抽取",
            "evidence": (
                f"抽取到模型树证据 {content_totals.get('model_tree_items', 0)} 条；"
                f"几何={len(case_content.get('geometry', []))}，"
                f"物理场={len(case_content.get('physics', []))}，"
                f"材料={len(case_content.get('materials', []))}，"
                f"网格={len(case_content.get('mesh', []))}，"
                f"研究={len(case_content.get('studies', []))}，"
                f"结果={len(case_content.get('results', []))}。"
            ),
            "judgement": (
                "模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。"
                if content_totals.get("model_tree_items", 0)
                else "当前文件内容中尚未自动抽取到明确模型树结构；需要补充脚本、MPH 摘要或更完整文本。"
            ),
        },
        {
            "step": "3. 建模脚本识别",
            "evidence": (
                "检测到可复用的 MATLAB/Java 建模脚本："
                + (", ".join(script_names) if script_names else "未检测到 MATLAB/Java 脚本")
            ),
            "judgement": (
                "脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。"
                if has_scripts
                else "缺少脚本时，只能依赖文档和其他文本线索推断建模逻辑。"
            ),
        },
        {
            "step": "4. 参数与约束提取",
            "evidence": f"从文本、MATLAB 或 Java 证据中提取到 {len(parameters)} 个参数。",
            "judgement": (
                "这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。"
                if parameters
                else "暂未发现显式参数，需要人工补充参数范围或从 COMSOL/LiveLink 中进一步导出。"
            ),
        },
        {
            "step": "5. 理论与模型来源判断",
            "evidence": (
                f"PDF 文档={file_summary.get('pdf_files', 0)}，"
                f"MPH 模型={file_summary.get('mph_files', 0)}。"
            ),
            "judgement": _theory_and_model_judgement(has_pdf, has_mph),
        },
        {
            "step": "6. 训练阶段判断",
            "evidence": f"CSV 训练数据文件数量为 {file_summary.get('csv_files', 0)}。",
            "judgement": (
                "已有 CSV，可继续检查输入/输出列并训练本地代理模型。"
                if has_csv
                else "当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。"
            ),
        },
        {
            "step": "7. 记忆库补充",
            "evidence": f"案例标题为 {card.get('title', 'case')}，训练阶段为 {card.get('training_stage', 'unknown')}。",
            "judgement": "该案例的文件摘要、参数、建模逻辑和下一步动作会写入案例知识库，并可被后续自动建模方案检索复用。",
        },
    ]
    return trace


def _theory_and_model_judgement(has_pdf: bool, has_mph: bool) -> str:
    if has_pdf and has_mph:
        return "PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。"
    if has_pdf:
        return "PDF 可提供理论、假设和操作流程，但缺少 MPH 时需要用脚本或人工步骤重建模型。"
    if has_mph:
        return "MPH 是权威模型文件，但缺少 PDF 时理论背景和验证目标需要从脚本、文件名或后续人工说明补充。"
    return "未检测到 PDF 或 MPH，当前判断主要依赖脚本文本和参数线索。"


def _reusable_confidence(
    has_scripts: bool,
    has_pdf: bool,
    has_mph: bool,
    parameters: list[dict[str, str]],
    has_csv: bool,
) -> str:
    score = int(has_scripts) + int(has_pdf) + int(has_mph) + int(bool(parameters)) + int(has_csv)
    if score >= 4:
        return "high"
    if score >= 2:
        return "medium"
    return "low"


def _gaps(has_training_csv: bool, has_mph: bool, parameters: list[dict[str, str]]) -> list[str]:
    gaps = []
    if not has_training_csv:
        gaps.append("Missing parameter-sweep CSV for numerical surrogate training.")
    if has_mph:
        gaps.append("MPH files need COMSOL with MATLAB summaries for reliable internal settings.")
    if not parameters:
        gaps.append("No parameter table was detected; parameters may need manual extraction from scripts or PDFs.")
    return gaps or ["No major gap detected from available files."]


def _upsert_index(index_path: Path, card: dict[str, Any], json_path: Path, md_path: Path) -> None:
    if index_path.exists():
        index = json.loads(index_path.read_text(encoding="utf-8"))
    else:
        index = {"kind": "comsol_case_knowledge_index", "cases": []}

    entry = {
        "title": card["title"],
        "case_dir": card["case_dir"],
        "training_stage": card["training_stage"],
        "json": str(json_path),
        "markdown": str(md_path),
        "updated_at": card["created_at"],
        "file_summary": card["file_summary"],
    }
    cases = [
        case
        for case in index.get("cases", [])
        if case.get("case_dir") != card["case_dir"] and case.get("title") != card["title"]
    ]
    cases.append(entry)
    index["cases"] = sorted(cases, key=lambda item: item["title"])
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def _slugify(value: str) -> str:
    slug = re.sub(r"[^\w\u4e00-\u9fff._-]+", "_", value.strip(), flags=re.UNICODE)
    return slug.strip("_") or "comsol_case"
