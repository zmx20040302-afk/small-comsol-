from __future__ import annotations

import argparse
import json
import socket
import sys
import traceback
import webbrowser
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from comsol_small_model.constraints import validate_constraints
from comsol_small_model.article_knowledge import summarize_article_docx
from comsol_small_model.case_knowledge import summarize_case_directory
from comsol_small_model.case_memory import generate_model_plan, remember_case
from comsol_small_model.code_generator import generate_comsol_code_from_memory
from comsol_small_model.file_reader import (
    build_learning_summary,
    summarize_file,
    summarize_files,
    summarize_uploaded_text,
    summarize_uploaded_texts,
)
from comsol_small_model.instruction_agent import respond_to_instruction
from comsol_small_model.livelink_builder import build_livelink_script_from_constraints
from comsol_small_model.matlab_reader import inspect_matlab_file
from comsol_small_model.work_feedback import append_work_log, build_work_feedback


GENERATED_DIR = ROOT / "generated"
MODELS_DIR = ROOT / "models"
WORK_LOG_PATH = GENERATED_DIR / "work_logs.jsonl"


class AppHandler(BaseHTTPRequestHandler):
    server_version = "ComsolSmallModelWeb/0.1"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self._send_html(CONVERSATIONAL_INDEX)
        elif parsed.path == "/api/default-constraints":
            self._send_json(json.loads((ROOT / "configs" / "thermal_constraints.json").read_text(encoding="utf-8")))
        else:
            self.send_error(404, "Not found")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        self._active_endpoint = parsed.path
        self._active_request_payload = {}
        try:
            payload = self._read_json()
            self._active_request_payload = payload
            if parsed.path == "/api/inspect-matlab":
                self._inspect_matlab(payload)
            elif parsed.path == "/api/validate-constraints":
                self._validate_constraints(payload)
            elif parsed.path == "/api/generate-matlab":
                self._generate_matlab(payload)
            elif parsed.path == "/api/generate-comsol-code":
                self._generate_comsol_code(payload)
            elif parsed.path == "/api/train":
                self._train(payload)
            elif parsed.path == "/api/read-file":
                self._read_file(payload)
            elif parsed.path == "/api/read-files":
                self._read_files(payload)
            elif parsed.path == "/api/read-uploaded-file":
                self._read_uploaded_file(payload)
            elif parsed.path == "/api/read-uploaded-files":
                self._read_uploaded_files(payload)
            elif parsed.path == "/api/instruction":
                self._instruction(payload)
            elif parsed.path == "/api/learning-summary":
                self._learning_summary(payload)
            elif parsed.path == "/api/learn-case":
                self._learn_case(payload)
            elif parsed.path == "/api/learn-article":
                self._learn_article(payload)
            elif parsed.path == "/api/plan-model":
                self._plan_model(payload)
            else:
                self.send_error(404, "Not found")
        except Exception as exc:  # noqa: BLE001
            self._send_json(
                {
                    "ok": False,
                    "error": str(exc),
                    "trace": traceback.format_exc(limit=2),
                },
                status=400,
            )

    def log_message(self, fmt: str, *args: object) -> None:
        print(fmt % args)

    def _inspect_matlab(self, payload: dict[str, object]) -> None:
        path = _resolve_user_path(str(payload.get("path", "")))
        summary = inspect_matlab_file(path)
        self._send_json({"ok": True, "summary": json.loads(summary.to_json())})

    def _validate_constraints(self, payload: dict[str, object]) -> None:
        cfg = _constraints_from_payload(payload)
        validate_constraints(cfg)
        self._send_json({"ok": True, "message": "constraints are valid"})

    def _generate_matlab(self, payload: dict[str, object]) -> None:
        cfg = _constraints_from_payload(payload)
        validate_constraints(cfg)
        script = build_livelink_script_from_constraints(cfg)
        GENERATED_DIR.mkdir(exist_ok=True)
        output_name = _safe_file_name(str(payload.get("output_name") or f"generated_build_{cfg['model_name']}.m"))
        if not output_name.endswith(".m"):
            output_name += ".m"
        output_path = GENERATED_DIR / output_name
        output_path.write_text(script, encoding="utf-8")
        self._send_json({"ok": True, "path": str(output_path), "script": script})

    def _generate_comsol_code(self, payload: dict[str, object]) -> None:
        requirement = str(payload.get("requirement", "")).strip()
        if not requirement:
            raise ValueError("requirement is empty")
        result = generate_comsol_code_from_memory(
            requirement=requirement,
            memory_path=str(payload.get("memory_path", "generated/case_memory/case_memory.json")),
            output_dir=str(payload.get("output_dir", GENERATED_DIR / "code")),
            output_prefix=_safe_file_name(str(payload.get("output_prefix") or "generated_comsol_model")),
            top_k=int(payload.get("top_k", 5)),
            existing_content=str(payload.get("existing_content", "")),
        )
        self._send_json({"ok": True, **result.as_dict()})

    def _train(self, payload: dict[str, object]) -> None:
        try:
            from comsol_small_model.surrogate import train_surrogate
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                f"Missing dependency {exc.name}. Run: pip install -r requirements.txt"
            ) from exc

        csv_path = _resolve_user_path(str(payload.get("csv_path", "")))
        input_columns = _split_columns(str(payload.get("input_columns", "")))
        output_columns = _split_columns(str(payload.get("output_columns", "")))
        MODELS_DIR.mkdir(exist_ok=True)
        model_name = _safe_file_name(str(payload.get("model_name") or "model.joblib"))
        if not model_name.endswith(".joblib"):
            model_name += ".joblib"
        model_path = MODELS_DIR / model_name
        report = train_surrogate(csv_path, model_path, input_columns, output_columns)
        self._send_json({"ok": True, "model_path": str(model_path), "report": asdict(report)})

    def _read_file(self, payload: dict[str, object]) -> None:
        path = _resolve_user_path(str(payload.get("path", "")))
        summary = summarize_file(path)
        self._send_json({"ok": True, "summary": summary.as_dict()})

    def _read_files(self, payload: dict[str, object]) -> None:
        raw_paths = payload.get("paths", [])
        if isinstance(raw_paths, str):
            raw_paths = _split_lines(raw_paths)
        if not isinstance(raw_paths, list) or not raw_paths:
            raise ValueError("paths must be a non-empty list")
        paths = [_resolve_user_path(str(path)) for path in raw_paths]
        summary = summarize_files(paths)
        self._send_json({"ok": True, "summary": summary})

    def _read_uploaded_file(self, payload: dict[str, object]) -> None:
        name = str(payload.get("name", "uploaded.txt"))
        content = str(payload.get("content", ""))
        summary = summarize_uploaded_text(name, content)
        self._send_json({"ok": True, "summary": summary.as_dict()})

    def _read_uploaded_files(self, payload: dict[str, object]) -> None:
        files = payload.get("files", [])
        if not isinstance(files, list) or not files:
            raise ValueError("files must be a non-empty list")
        normalized = []
        for file in files:
            if not isinstance(file, dict):
                raise ValueError("each uploaded file must be an object")
            normalized.append({"name": str(file.get("name", "uploaded.txt")), "content": str(file.get("content", ""))})
        summary = summarize_uploaded_texts(normalized)
        self._send_json({"ok": True, "summary": summary})

    def _instruction(self, payload: dict[str, object]) -> None:
        instruction = str(payload.get("instruction", ""))
        file_summary = payload.get("file_summary")
        if file_summary is not None and not isinstance(file_summary, dict):
            raise ValueError("file_summary must be an object")
        model_plan = None
        if instruction.strip():
            try:
                model_plan = generate_model_plan(
                    instruction,
                    str(payload.get("memory_path", "generated/case_memory/case_memory.json")),
                    int(payload.get("top_k", 3)),
                )
            except Exception as exc:  # noqa: BLE001
                model_plan = {"error": str(exc), "matched_cases": [], "case_count": 0}
        response = respond_to_instruction(instruction, file_summary, model_plan)
        self._send_json({"ok": True, "response": response})

    def _learning_summary(self, payload: dict[str, object]) -> None:
        file_summary = payload.get("file_summary")
        if not isinstance(file_summary, dict):
            raise ValueError("file_summary must be an object")
        self._send_json({"ok": True, "summary": build_learning_summary(file_summary)})

    def _learn_case(self, payload: dict[str, object]) -> None:
        case_dir = _resolve_user_path(str(payload.get("case_dir", "")))
        title = str(payload.get("title", "")).strip() or None
        output_dir = str(payload.get("output_dir", "generated/case_knowledge"))
        memory_path = str(payload.get("memory_path", "generated/case_memory/case_memory.json"))
        result = summarize_case_directory(case_dir, title=title, output_dir=output_dir)
        memory = remember_case(result["card"], memory_path)
        summary = result["card"].get("post_learning_summary", {})
        self._send_json(
            {
                "ok": True,
                "card": result["card"],
                "summary": summary,
                "outputs": result["outputs"],
                "memory": {
                    "path": memory["memory_path"],
                    "case_count": memory["case_count"],
                },
            }
        )

    def _learn_article(self, payload: dict[str, object]) -> None:
        article_path = _resolve_user_path(str(payload.get("article_path", "")))
        output_dir = str(payload.get("output_dir", "generated/article_knowledge"))
        memory_path = str(payload.get("memory_path", "generated/case_memory/case_memory.json"))
        result = summarize_article_docx(article_path, output_dir=output_dir, memory_path=memory_path)
        self._send_json({"ok": True, "card": result["card"], "outputs": result["outputs"]})

    def _plan_model(self, payload: dict[str, object]) -> None:
        requirement = str(payload.get("requirement", "")).strip()
        if not requirement:
            raise ValueError("requirement is empty")
        memory_path = str(payload.get("memory_path", "generated/case_memory/case_memory.json"))
        top_k = int(payload.get("top_k", 5))
        self._send_json({"ok": True, "plan": generate_model_plan(requirement, memory_path, top_k)})

    def _read_json(self) -> dict[str, object]:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw or "{}")

    def _send_json(self, payload: object, status: int = 200) -> None:
        if isinstance(payload, dict) and getattr(self, "_active_endpoint", "").startswith("/api/"):
            payload = self._with_work_feedback(payload)
        data = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _with_work_feedback(self, payload: dict[str, object]) -> dict[str, object]:
        if "work_feedback" in payload:
            return payload
        endpoint = getattr(self, "_active_endpoint", "")
        request_payload = getattr(self, "_active_request_payload", {})
        feedback = build_work_feedback(endpoint, request_payload, payload)
        enriched = dict(payload)
        enriched["work_feedback"] = feedback
        append_work_log(WORK_LOG_PATH, feedback)
        return enriched

    def _send_html(self, html: str) -> None:
        data = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def _constraints_from_payload(payload: dict[str, object]) -> dict[str, object]:
    text = str(payload.get("constraints_json", "")).strip()
    if not text:
        raise ValueError("constraints_json is empty")
    return json.loads(text)


def _resolve_user_path(value: str) -> Path:
    if not value:
        raise ValueError("path is empty")
    path = Path(value)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if not path.exists():
        raise FileNotFoundError(str(path))
    return path


def _safe_file_name(value: str) -> str:
    keep = []
    for char in value.strip():
        if char.isalnum() or char in "._-":
            keep.append(char)
    name = "".join(keep)
    return name or "generated.m"


def _split_columns(value: str) -> list[str]:
    return [part for part in value.replace(",", " ").split() if part]


def _split_lines(value: str) -> list[str]:
    return [part.strip() for part in value.replace(";", "\n").splitlines() if part.strip()]


def run(host: str = "127.0.0.1", port: int = 8765, open_browser: bool = False) -> None:
    server = None
    selected_port = port
    for candidate in range(port, port + 20):
        try:
            server = ThreadingHTTPServer((host, candidate), AppHandler)
            selected_port = candidate
            break
        except OSError:
            continue
    if server is None:
        raise OSError(f"No free port found from {port} to {port + 19}")

    display_host = "127.0.0.1" if host in {"0.0.0.0", "::"} else host
    url = f"http://{display_host}:{selected_port}"
    if open_browser:
        webbrowser.open(url)
    print(f"COMSOL small model web app: {url}")
    if host == "0.0.0.0":
        print("LAN access URLs:")
        for address in _local_ipv4_addresses():
            print(f"  http://{address}:{selected_port}")
        print("Warning: LAN mode exposes file-reading and model-generation APIs to your local network.")
    server.serve_forever()


def _local_ipv4_addresses() -> list[str]:
    addresses = {"127.0.0.1"}
    try:
        hostname = socket.gethostname()
        for item in socket.getaddrinfo(hostname, None, family=socket.AF_INET):
            addresses.add(item[4][0])
    except OSError:
        pass
    return sorted(addresses)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the COMSOL small model web app")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host. Use 0.0.0.0 for LAN access.")
    parser.add_argument("--port", type=int, default=8765, help="Starting port. The app tries the next 19 ports if busy.")
    parser.add_argument("--open", action="store_true", help="Open the local URL in the default browser.")
    return parser.parse_args(argv)


INDEX_HTML = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>COMSOL Small Model</title>
  <style>
    :root {
      --ink: #182026;
      --muted: #5e6a70;
      --line: #ccd5d9;
      --panel: #f6f8f8;
      --accent: #0f766e;
      --accent-2: #9a3412;
      --ok: #166534;
      --bad: #991b1b;
      --white: #ffffff;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      color: var(--ink);
      background: var(--white);
      font: 14px/1.5 "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
    }
    header {
      min-height: 112px;
      padding: 28px 32px 24px;
      color: white;
      background:
        linear-gradient(90deg, rgba(15, 118, 110, .95), rgba(154, 52, 18, .82)),
        repeating-linear-gradient(135deg, rgba(255,255,255,.15) 0 1px, transparent 1px 14px);
    }
    h1 { margin: 0; font-size: 28px; font-weight: 680; letter-spacing: 0; }
    .sub { margin-top: 6px; color: rgba(255,255,255,.86); }
    main {
      display: grid;
      grid-template-columns: minmax(280px, 420px) minmax(420px, 1fr);
      gap: 0;
      min-height: calc(100vh - 112px);
    }
    nav {
      border-right: 1px solid var(--line);
      background: var(--panel);
      padding: 18px;
    }
    section {
      padding: 22px 26px;
      border-bottom: 1px solid var(--line);
    }
    h2 { margin: 0 0 14px; font-size: 17px; font-weight: 650; }
    label { display: block; margin: 10px 0 5px; color: var(--muted); font-size: 12px; }
    input, textarea {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 9px 10px;
      color: var(--ink);
      background: white;
      font: inherit;
    }
    textarea {
      min-height: 260px;
      resize: vertical;
      font-family: Consolas, "Courier New", monospace;
      font-size: 12px;
    }
    textarea.compact { min-height: 120px; }
    button {
      min-height: 36px;
      border: 1px solid transparent;
      border-radius: 6px;
      padding: 7px 12px;
      color: white;
      background: var(--accent);
      font-weight: 620;
      cursor: pointer;
    }
    button.secondary { background: var(--accent-2); }
    button.ghost {
      color: var(--ink);
      background: white;
      border-color: var(--line);
    }
    .row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-top: 12px; }
    .workspace {
      display: grid;
      grid-template-rows: auto 1fr;
      min-width: 0;
    }
    .output {
      padding: 18px 26px 26px;
      min-width: 0;
    }
    pre {
      min-height: 420px;
      overflow: auto;
      margin: 0;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #101820;
      color: #d6f3e9;
      font: 12px/1.45 Consolas, "Courier New", monospace;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .status { margin-top: 10px; min-height: 20px; color: var(--muted); }
    .status.ok { color: var(--ok); }
    .status.bad { color: var(--bad); }
    @media (max-width: 860px) {
      main { grid-template-columns: 1fr; }
      nav { border-right: 0; border-bottom: 1px solid var(--line); }
      header { padding: 22px 20px; }
      section, .output { padding-left: 18px; padding-right: 18px; }
    }
  </style>
</head>
<body>
  <header>
    <h1>COMSOL 小模型工作台</h1>
    <div class="sub">MATLAB 读取 · 约束建模 · LiveLink 生成 · 代理模型训练</div>
  </header>
  <main>
    <nav>
      <section>
        <h2>语言指令</h2>
        <label for="instruction">输入你的需求</label>
        <textarea id="instruction" class="compact">请读取文件，并判断能否用于 COMSOL 自动建模和代理模型训练。</textarea>
        <div class="row">
          <button onclick="sendInstruction()">获取反馈</button>
        </div>
      </section>
      <section>
        <h2>文件输入</h2>
        <label for="filePath">文件路径</label>
        <input id="filePath" value="../acoustic_rectangular_cavity/build_acoustic_rectangular_cavity.m">
        <label for="uploadFile">选择文件</label>
        <input id="uploadFile" type="file">
        <div class="row">
          <button onclick="readFilePath()">读取路径</button>
          <button class="ghost" onclick="readUploadedFile()">读取选择文件</button>
        </div>
      </section>
      <section>
        <h2>MATLAB 文件</h2>
        <label for="matlabPath">.m 路径</label>
        <input id="matlabPath" value="../acoustic_rectangular_cavity/build_acoustic_rectangular_cavity.m">
        <div class="row">
          <button onclick="inspectMatlab()">读取</button>
        </div>
      </section>
      <section>
        <h2>约束配置</h2>
        <textarea id="constraints"></textarea>
        <div class="row">
          <button class="ghost" onclick="loadDefaults()">载入示例</button>
          <button onclick="validateConstraints()">校验</button>
          <button class="secondary" onclick="generateMatlab()">生成 MATLAB</button>
        </div>
      </section>
      <section>
        <h2>训练</h2>
        <label for="csvPath">CSV 路径</label>
        <input id="csvPath" value="examples/sample_comsol_data.csv">
        <label for="inputs">输入列</label>
        <input id="inputs" value="k Q h L">
        <label for="outputs">输出列</label>
        <input id="outputs" value="Tmax Tavg">
        <label for="modelName">模型文件名</label>
        <input id="modelName" value="thermal_surrogate.joblib">
        <div class="row">
          <button onclick="trainModel()">训练</button>
        </div>
      </section>
    </nav>
    <div class="workspace">
      <section>
        <h2>结果</h2>
        <div id="status" class="status">ready</div>
      </section>
      <div class="output">
        <pre id="output">{}</pre>
      </div>
    </div>
  </main>
  <script>
    const output = document.getElementById("output");
    const statusBox = document.getElementById("status");
    const constraints = document.getElementById("constraints");
    let lastFileSummary = null;

    async function request(path, body) {
      statusBox.className = "status";
      statusBox.textContent = "running";
      const response = await fetch(path, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
      });
      const data = await response.json();
      output.textContent = JSON.stringify(data, null, 2);
      statusBox.className = data.ok === false ? "status bad" : "status ok";
      statusBox.textContent = data.ok === false ? "failed" : "done";
      return data;
    }

    async function loadDefaults() {
      const response = await fetch("/api/default-constraints");
      const data = await response.json();
      constraints.value = JSON.stringify(data, null, 2);
      output.textContent = constraints.value;
      statusBox.className = "status ok";
      statusBox.textContent = "loaded";
    }

    function inspectMatlab() {
      return request("/api/inspect-matlab", {path: document.getElementById("matlabPath").value});
    }

    async function readFilePath() {
      const data = await request("/api/read-file", {path: document.getElementById("filePath").value});
      if (data.ok) {
        lastFileSummary = data.summary;
      }
      return data;
    }

    async function readUploadedFile() {
      const file = document.getElementById("uploadFile").files[0];
      if (!file) {
        output.textContent = JSON.stringify({ok: false, error: "No file selected"}, null, 2);
        statusBox.className = "status bad";
        statusBox.textContent = "failed";
        return;
      }
      const content = await file.text();
      const data = await request("/api/read-uploaded-file", {name: file.name, content});
      if (data.ok) {
        lastFileSummary = data.summary;
      }
      return data;
    }

    function sendInstruction() {
      return request("/api/instruction", {
        instruction: document.getElementById("instruction").value,
        file_summary: lastFileSummary
      });
    }

    function validateConstraints() {
      return request("/api/validate-constraints", {constraints_json: constraints.value});
    }

    function generateMatlab() {
      let name = "generated_build_thermal_rectangle_surrogate.m";
      try {
        const cfg = JSON.parse(constraints.value);
        name = "generated_build_" + cfg.model_name + ".m";
      } catch (err) {}
      return request("/api/generate-matlab", {constraints_json: constraints.value, output_name: name});
    }

    function trainModel() {
      return request("/api/train", {
        csv_path: document.getElementById("csvPath").value,
        input_columns: document.getElementById("inputs").value,
        output_columns: document.getElementById("outputs").value,
        model_name: document.getElementById("modelName").value
      });
    }

    loadDefaults();
  </script>
</body>
</html>
"""


CONVERSATIONAL_INDEX = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>COMSOL Conversational Model</title>
  <style>
    :root {
      --bg: #f7f7f5;
      --surface: #ffffff;
      --surface-2: #f0f2f2;
      --ink: #1f2328;
      --muted: #646b72;
      --line: #d8dadd;
      --accent: #0f766e;
      --accent-dark: #0b5f59;
      --warn: #9a3412;
      --bad: #991b1b;
      --code-bg: #111827;
      --code-ink: #d1fae5;
    }
    * { box-sizing: border-box; }
    html, body { height: 100%; overflow: hidden; }
    body {
      margin: 0;
      color: var(--ink);
      background: var(--bg);
      font: 14px/1.5 "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
    }
    button, input, textarea { font: inherit; }
    button {
      min-height: 34px;
      border: 1px solid var(--line);
      border-radius: 7px;
      padding: 7px 11px;
      color: var(--ink);
      background: var(--surface);
      cursor: pointer;
    }
    button.primary {
      border-color: var(--accent);
      color: #fff;
      background: var(--accent);
      font-weight: 650;
    }
    button.primary:hover { background: var(--accent-dark); }
    button.warning {
      border-color: var(--warn);
      color: #fff;
      background: var(--warn);
    }
    input, textarea {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 7px;
      padding: 8px 10px;
      color: var(--ink);
      background: var(--surface);
    }
    textarea {
      min-height: 96px;
      resize: vertical;
    }
    label {
      display: block;
      margin: 10px 0 5px;
      color: var(--muted);
      font-size: 12px;
    }
    .app {
      display: grid;
      grid-template-columns: 240px minmax(0, 1fr) 360px;
      height: 100vh;
      max-height: 100vh;
      min-height: 640px;
      overflow: hidden;
    }
    .rail {
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--line);
      background: #ecefed;
      min-width: 0;
    }
    .brand {
      padding: 18px 16px 14px;
      border-bottom: 1px solid var(--line);
    }
    .brand-title {
      margin: 0;
      font-size: 16px;
      font-weight: 720;
      letter-spacing: 0;
    }
    .brand-subtitle {
      margin-top: 4px;
      color: var(--muted);
      font-size: 12px;
    }
    .thread-list {
      padding: 10px;
      overflow: auto;
    }
    .thread {
      width: 100%;
      margin-bottom: 8px;
      text-align: left;
      background: transparent;
    }
    .thread.active {
      border-color: #b8c7c4;
      background: #fff;
      font-weight: 650;
    }
    .rail-foot {
      margin-top: auto;
      padding: 12px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 12px;
    }
    .chat {
      display: grid;
      grid-template-rows: auto minmax(0, 1fr) auto;
      min-width: 0;
      min-height: 0;
      background: var(--surface);
    }
    .chat-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 14px 20px;
      border-bottom: 1px solid var(--line);
    }
    .chat-title {
      font-size: 15px;
      font-weight: 700;
    }
    .status {
      color: var(--muted);
      font-size: 12px;
    }
    .status.ok { color: var(--accent-dark); }
    .status.bad { color: var(--bad); }
    .messages {
      overflow: auto;
      min-height: 0;
      padding: 20px 24px 18px;
      scroll-behavior: smooth;
    }
    .message {
      display: grid;
      grid-template-columns: 34px minmax(0, 1fr);
      gap: 12px;
      max-width: 920px;
      margin: 0 auto 22px;
    }
    .avatar {
      display: grid;
      place-items: center;
      width: 32px;
      height: 32px;
      border: 1px solid var(--line);
      border-radius: 50%;
      color: var(--muted);
      background: var(--surface-2);
      font-size: 12px;
      font-weight: 700;
    }
    .message.user .avatar {
      color: #fff;
      background: var(--accent);
      border-color: var(--accent);
    }
    .bubble {
      min-width: 0;
      padding-top: 4px;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .bubble h3 {
      margin: 0 0 6px;
      font-size: 14px;
    }
    .bubble ul {
      margin: 6px 0 0;
      padding-left: 18px;
    }
    .bubble code {
      padding: 1px 4px;
      border-radius: 4px;
      background: var(--surface-2);
      font-family: Consolas, "Courier New", monospace;
      font-size: 12px;
    }
    .composer {
      padding: 14px 20px 18px;
      border-top: 1px solid var(--line);
      background: var(--surface);
    }
    .composer-inner {
      max-width: 920px;
      margin: 0 auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
      overflow: hidden;
    }
    #prompt {
      min-height: 78px;
      max-height: 220px;
      border: 0;
      border-radius: 0;
      outline: 0;
      resize: vertical;
    }
    .composer-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 8px;
      border-top: 1px solid var(--line);
      background: #fafafa;
    }
    .quick-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .tools {
      border-left: 1px solid var(--line);
      background: #f4f5f4;
      overflow: auto;
      min-width: 0;
      min-height: 0;
      height: 100vh;
      max-height: 100vh;
      overscroll-behavior: contain;
    }
    .tool-section {
      padding: 16px;
      border-bottom: 1px solid var(--line);
    }
    .tool-title {
      margin: 0 0 10px;
      font-size: 13px;
      font-weight: 720;
      text-transform: uppercase;
      color: var(--muted);
    }
    .row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      margin-top: 10px;
    }
    #constraints {
      min-height: 230px;
      font-family: Consolas, "Courier New", monospace;
      font-size: 12px;
    }
    .raw {
      min-height: 170px;
      max-height: 360px;
      overflow: auto;
      margin: 0;
      padding: 11px;
      border: 1px solid var(--line);
      border-radius: 7px;
      color: var(--code-ink);
      background: var(--code-bg);
      font: 12px/1.45 Consolas, "Courier New", monospace;
      white-space: pre-wrap;
      word-break: break-word;
    }
    @media (max-width: 1180px) {
      .app { grid-template-columns: 210px minmax(0, 1fr); }
      .tools {
        grid-column: 1 / -1;
        border-left: 0;
        border-top: 1px solid var(--line);
        max-height: 48vh;
        height: 48vh;
      }
    }
    @media (max-width: 760px) {
      .app {
        grid-template-columns: 1fr;
        height: auto;
        min-height: 100vh;
        max-height: none;
        overflow: visible;
      }
      .rail { display: none; }
      .chat { min-height: 100vh; }
      .tools { height: auto; max-height: none; }
      .messages { padding: 16px; }
      .message { grid-template-columns: 28px minmax(0, 1fr); gap: 9px; }
      .avatar { width: 28px; height: 28px; }
    }
  </style>
</head>
<body>
  <div class="app">
    <aside class="rail">
      <div class="brand">
        <h1 class="brand-title">COMSOL Model Codex</h1>
        <div class="brand-subtitle">对话式建模与训练工作台</div>
      </div>
      <div class="thread-list">
        <button class="thread active" data-mode="chat" onclick="selectThreadMode('chat')">当前会话</button>
        <button class="thread" data-mode="modeling" onclick="selectThreadMode('modeling')">自动建模</button>
        <button class="thread" data-mode="reading" onclick="selectThreadMode('reading')">文件阅读</button>
        <button class="thread" data-mode="training" onclick="selectThreadMode('training')">代理模型训练</button>
      </div>
      <div class="rail-foot">本地运行：Python + COMSOL LiveLink MATLAB 脚本生成</div>
    </aside>

    <main class="chat">
      <header class="chat-header">
        <div>
          <div class="chat-title">COMSOL 训练对话助手</div>
          <div class="status" id="status">ready</div>
        </div>
        <button onclick="clearChat()">清空对话</button>
      </header>
      <div class="messages" id="messages"></div>
      <footer class="composer">
        <div class="composer-inner">
          <textarea id="prompt" placeholder="输入需求，例如：读取这个 MATLAB 文件，并判断能否用于自动建模和代理模型训练。"></textarea>
          <div class="composer-actions">
            <div class="quick-actions">
              <button onclick="useTemplate('请读取文件，并判断能否用于 COMSOL 自动建模和代理模型训练。')">读取文件</button>
              <button onclick="useTemplate('根据当前约束生成 COMSOL LiveLink MATLAB 建模脚本。')">生成脚本</button>
              <button onclick="useTemplate('根据 CSV 数据训练代理模型，并说明输入列和输出列。')">训练建议</button>
              <button onclick="useTemplate('总结当前案例学到的建模理论、参数、约束、可复用功能和下一步训练路径。')">学习总结</button>
              <button onclick="planModelFromPrompt()">建模方案</button>
            </div>
            <button class="primary" onclick="sendPrompt()">发送</button>
          </div>
        </div>
      </footer>
    </main>

    <aside class="tools">
      <section class="tool-section" id="tool-files">
        <h2 class="tool-title">文件</h2>
        <label for="filePath">路径，每行一个</label>
        <textarea id="filePath" oninput="syncCaseFieldsFromPaths()" onchange="syncCaseFieldsFromPaths()">../acoustic_rectangular_cavity/build_acoustic_rectangular_cavity.m
examples/sample_comsol_data.csv
configs/thermal_constraints.json</textarea>
        <label for="uploadFile">选择文件，可多选</label>
        <input id="uploadFile" type="file" multiple onchange="syncCaseFieldsFromUpload()">
        <div class="row">
          <button onclick="readFilePath()">读取路径文件</button>
          <button onclick="readUploadedFile()">读取选择文件</button>
          <button onclick="buildLearningSummary()">学习总结</button>
        </div>
        <label for="caseDir">COMSOL 案例目录</label>
        <input id="caseDir" value="D:/桌面/codex/案例下载/COMSOL/科赫雪花建模" oninput="syncCaseTitleFromCaseDir()" onchange="syncCaseTitleFromCaseDir()">
        <label for="caseTitle">案例名称</label>
        <input id="caseTitle" value="科赫雪花建模">
        <label for="caseSyncInfo">自动关联信息</label>
        <input id="caseSyncInfo" value="等待选择文件或输入路径" readonly>
        <div class="row">
          <button class="primary" onclick="learnCaseDirectory()">学习案例并输出总结</button>
        </div>
        <label for="articlePath">文章/论文 Word 路径</label>
        <input id="articlePath" value="D:/桌面/COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究.docx">
        <div class="row">
          <button onclick="learnArticleDocument()">按文章生成建模修正方案</button>
        </div>
      </section>
      <section class="tool-section" id="tool-matlab">
        <h2 class="tool-title">MATLAB</h2>
        <label for="matlabPath">.m 路径</label>
        <input id="matlabPath" value="../acoustic_rectangular_cavity/build_acoustic_rectangular_cavity.m">
        <label for="codeRequirement">COMSOL 建模需求</label>
        <textarea id="codeRequirement">结合已学习案例和文章知识，生成一个 COMSOL 模型构建脚本，要求同时输出 LiveLink MATLAB 代码和 Java 代码，并标注需要人工复核的边界选择、材料和物理场。</textarea>
        <label for="existingComsolContent">现有 MATLAB/Java/模型摘要内容</label>
        <textarea id="existingComsolContent" placeholder="可粘贴已有 COMSOL MATLAB 脚本、Java 代码或 MPH 摘要；模型会根据学习库给出修正和完善建议。"></textarea>
        <div class="row">
          <button onclick="inspectMatlab()">解析 MATLAB</button>
          <button class="primary" onclick="generateComsolCode()">生成 MATLAB + Java</button>
        </div>
      </section>
      <section class="tool-section" id="tool-constraints">
        <h2 class="tool-title">约束</h2>
        <textarea id="constraints"></textarea>
        <div class="row">
          <button onclick="loadDefaults()">载入示例</button>
          <button onclick="validateConstraints()">校验</button>
          <button class="warning" onclick="generateMatlab()">生成 MATLAB</button>
        </div>
      </section>
      <section class="tool-section" id="tool-training">
        <h2 class="tool-title">训练</h2>
        <label for="csvPath">CSV 路径</label>
        <input id="csvPath" value="examples/sample_comsol_data.csv">
        <label for="inputs">输入列</label>
        <input id="inputs" value="k Q h L">
        <label for="outputs">输出列</label>
        <input id="outputs" value="Tmax Tavg">
        <label for="modelName">模型文件名</label>
        <input id="modelName" value="thermal_surrogate.joblib">
        <div class="row">
          <button class="primary" onclick="trainModel()">训练模型</button>
        </div>
      </section>
      <section class="tool-section">
        <h2 class="tool-title">原始响应</h2>
        <pre id="raw" class="raw">{}</pre>
      </section>
    </aside>
  </div>

  <script>
    const messages = document.getElementById("messages");
    const raw = document.getElementById("raw");
    const statusBox = document.getElementById("status");
    const constraints = document.getElementById("constraints");
    let lastFileSummary = null;

    function setStatus(text, kind) {
      statusBox.textContent = text;
      statusBox.className = "status" + (kind ? " " + kind : "");
    }

    function escapeHtml(value) {
      return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;");
    }

    function addMessage(role, html) {
      const message = document.createElement("div");
      message.className = "message " + role;
      const avatar = role === "user" ? "你" : "AI";
      message.innerHTML = `<div class="avatar">${avatar}</div><div class="bubble">${html}</div>`;
      messages.appendChild(message);
      jumpToLatestMessage();
    }

    function jumpToLatestMessage() {
      const latest = messages.lastElementChild;
      if (latest) {
        latest.scrollIntoView({behavior: "smooth", block: "end"});
      }
      requestAnimationFrame(() => {
        messages.scrollTop = messages.scrollHeight;
      });
    }

    function renderJson(data) {
      raw.textContent = JSON.stringify(data, null, 2);
    }

    function summarizeWorkFeedback(data) {
      const feedback = data.work_feedback;
      if (!feedback) return "";
      const details = feedback.details || {};
      const next = (feedback.next_steps || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const detailLines = [];
      if (details.summary_kind) detailLines.push(`<li>摘要类型：<code>${escapeHtml(details.summary_kind)}</code></li>`);
      if (details.summary_name) detailLines.push(`<li>对象：<code>${escapeHtml(details.summary_name)}</code></li>`);
      if (details.output_path) detailLines.push(`<li>输出：<code>${escapeHtml(details.output_path)}</code></li>`);
      if (details.training_report) {
        detailLines.push(`<li>训练报告：<code>${escapeHtml(JSON.stringify(details.training_report))}</code></li>`);
      }
      return `<h3>本次工作反馈</h3><p>${escapeHtml(feedback.summary || "")}</p>${detailLines.length ? `<ul>${detailLines.join("")}</ul>` : ""}${next ? `<h3>建议下一步</h3><ul>${next}</ul>` : ""}`;
    }

    async function request(path, body) {
      setStatus("running", "");
      const response = await fetch(path, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
      });
      const data = await response.json();
      renderJson(data);
      setStatus(data.ok === false ? "failed" : "done", data.ok === false ? "bad" : "ok");
      const workFeedback = summarizeWorkFeedback(data);
      if (workFeedback) addMessage("assistant", workFeedback);
      jumpToLatestMessage();
      return data;
    }

    function summarizeInstructionResponse(data) {
      if (!data.ok) {
        return `<h3>执行失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      const response = data.response || {};
      if (response.assistant_message) {
        const paragraphs = escapeHtml(response.assistant_message)
          .split(/\n\s*\n/)
          .map(part => `<p>${part.replace(/\n/g, "<br>")}</p>`)
          .join("");
        const sections = (response.explanation_sections || []).map(section => {
          const items = (section.items || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
          return `<h3>${escapeHtml(section.title || "说明")}</h3><ul>${items}</ul>`;
        }).join("");
        const intents = (response.intent || []).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
        const tool = response.suggested_tool ? `<p>建议工具：<code>${escapeHtml(response.suggested_tool)}</code></p>` : "";
        return `<h3>COMSOL 训练讲解</h3>${paragraphs}${sections}<h3>识别到的任务</h3><p>${intents}</p>${tool}`;
      }
      const intents = (response.intent || []).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
      const feedback = (response.feedback || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const next = (response.next_actions || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      return `<h3>我理解到的任务</h3><p>${intents || "<code>general</code>"}</p><ul>${feedback}</ul>${next ? `<h3>下一步</h3><ul>${next}</ul>` : ""}`;
    }

    function summarizeFileResponse(data) {
      if (!data.ok) {
        return `<h3>读取失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      const summary = data.summary;
      const details = summary.details || {};
      if (summary.kind === "file_collection") {
        const files = (summary.files || []).map(file =>
          `<li><code>${escapeHtml(file.name)}</code> - ${escapeHtml(file.kind)} (${file.size_bytes} bytes)</li>`
        ).join("");
        const kinds = Object.entries(details.kinds || {})
          .map(([kind, count]) => `<code>${escapeHtml(kind)}</code>: ${count}`)
          .join(" ");
        return `<h3>已读取多个文件</h3><p>数量：${details.count || 0}</p><p>${kinds}</p><ul>${files}</ul>`;
      }
      let lines = [
        `<li>文件：<code>${escapeHtml(summary.name)}</code></li>`,
        `<li>类型：<code>${escapeHtml(summary.kind)}</code></li>`,
        `<li>大小：${summary.size_bytes} bytes</li>`
      ];
      if (summary.kind === "matlab_livelink") {
        lines.push(`<li>参数数量：${details.parameters || 0}</li>`);
      }
      if (summary.kind === "csv_table") {
        lines.push(`<li>列：<code>${escapeHtml((details.columns || []).join(", "))}</code></li>`);
      }
      return `<h3>文件已读取</h3><ul>${lines.join("")}</ul><h3>预览</h3><p>${escapeHtml(summary.preview || "").slice(0, 1200)}</p>`;
    }

    function summarizeGeneric(title, data) {
      if (!data.ok) {
        return `<h3>${title}失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      return `<h3>${title}完成</h3><p><code>${escapeHtml(JSON.stringify(data).slice(0, 700))}</code></p>`;
    }

    function summarizeComsolCodeResponse(data) {
      if (!data.ok) {
        return summarizeGeneric("COMSOL MATLAB + Java 生成", data);
      }
      const plan = data.plan || {};
      const outputs = data.outputs || {};
      const guidance = (data.theory_guidance || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const refinements = (data.refinement_suggestions || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const review = data.existing_content_review || {};
      const checks = review.checks || {};
      const reviewRows = Object.entries(checks)
        .map(([key, value]) => `<li>${escapeHtml(key)}：${value ? "已包含" : "缺失或未识别"}</li>`)
        .join("");
      const domains = (plan.inferred_domains || []).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
      const matches = (plan.matched_cases || [])
        .slice(0, 5)
        .map(item => `<li>${escapeHtml(item.title || "")}，score=${escapeHtml(item.score || 0)}</li>`)
        .join("");
      const limits = (plan.limitations || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      return `<h3>COMSOL MATLAB + Java 代码已生成</h3><ul><li>MATLAB：<code>${escapeHtml(outputs.matlab || "")}</code></li><li>Java：<code>${escapeHtml(outputs.java || "")}</code></li><li>理论指导报告：<code>${escapeHtml(outputs.guidance || "")}</code></li><li>推断物理域：${domains || "<code>unknown</code>"}</li></ul>${matches ? `<h3>引用的案例记忆</h3><ul>${matches}</ul>` : ""}${guidance ? `<h3>理论指导</h3><ul>${guidance}</ul>` : ""}${reviewRows ? `<h3>现有内容检查</h3><ul>${reviewRows}</ul>` : ""}${refinements ? `<h3>调整和完善建议</h3><ul>${refinements}</ul>` : ""}${limits ? `<h3>复核提醒</h3><ul>${limits}</ul>` : ""}<h3>学习过程/判断依据</h3><ul><li>先用需求检索案例记忆库，提取相似案例、参数、输出量和建模步骤。</li><li>再把推断出的物理场映射为 COMSOL LiveLink MATLAB 和 Java API 模板。</li><li>如果提供了现有脚本或模型摘要，会检查参数、几何、物理场、材料、网格、研究、结果和边界选择是否完整。</li><li>边界选择、材料属性和具体几何序列保留复核标注，便于后续用真实案例脚本修正。</li></ul>`;
    }

    function summarizeLearningResponse(data) {
      if (!data.ok) {
        return `<h3>学习总结失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      const summary = data.summary || {};
      const groups = summary.groups || {};
      const counts = Object.entries(groups)
        .map(([name, items]) => `<li><code>${escapeHtml(name)}</code>: ${Array.isArray(items) ? items.length : 0}</li>`)
        .join("");
      const recommendations = (summary.recommendations || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const workflow = (summary.workflow || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      return `<h3>COMSOL 文件学习总结</h3><ul>${counts}</ul><h3>建议</h3><ul>${recommendations}</ul><h3>实现路径</h3><ul>${workflow}</ul>`;
    }

    function summarizeCaseLearningResponse(data) {
      if (!data.ok) {
        return `<h3>案例学习失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      const card = data.card || {};
      const summary = data.summary || {};
      const fileSummary = card.file_summary || {};
      const caseContent = card.case_content || {};
      const contentTotals = caseContent.totals || {};
      const logic = (summary.learned_modeling_logic || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const trace = (summary.learning_trace || []).map(item => `<li><strong>${escapeHtml(item.step || "")}</strong><br><span>证据：${escapeHtml(item.evidence || "")}</span><br><span>判断：${escapeHtml(item.judgement || "")}</span></li>`).join("");
      const assets = (summary.reusable_assets || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const next = (summary.next_actions || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const params = (card.parameters || [])
        .slice(0, 20)
        .map(item => `<li><code>${escapeHtml(item.name)}</code> = <code>${escapeHtml(item.value || "")}</code> ${escapeHtml(item.description || "")}</li>`)
        .join("");
      const outputs = data.outputs || {};
      const memory = data.memory || {};
      const contentSections = ["geometry", "physics", "materials", "mesh", "studies", "results", "boundary_conditions"]
        .map(key => {
          const values = (caseContent[key] || []).slice(0, 10).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
          return values ? `<li>${escapeHtml(key)}：${values}</li>` : "";
        })
        .join("");
      const theoryKeywords = (caseContent.theory_keywords || []).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
      const sourceEvidence = (caseContent.source_extracts || [])
        .slice(0, 6)
        .map(item => `<li><code>${escapeHtml(item.name || "")}</code>：内容证据 ${escapeHtml(item.evidence_score || 0)} 条</li>`)
        .join("");
      const contentHtml = contentTotals.model_tree_items || contentSections || theoryKeywords
        ? `<h3>读取到的案例内容</h3><ul><li>模型树证据：${escapeHtml(contentTotals.model_tree_items || 0)} 条</li><li>已检查内容文件：${escapeHtml(contentTotals.source_files_checked || 0)} 个</li>${theoryKeywords ? `<li>理论关键词：${theoryKeywords}</li>` : ""}${contentSections}</ul>${sourceEvidence ? `<h3>文件内容证据</h3><ul>${sourceEvidence}</ul>` : ""}`
        : "";
      const alignment = card.knowledge_alignment || {};
      const externalCases = (alignment.case_matches || []).slice(0, 5).map(item => `<li><code>${escapeHtml(item.title || "")}</code> score=${escapeHtml(item.score || "")} 字段：${escapeHtml((item.supported_fields || []).join(", ") || "仅主题匹配")}</li>`).join("");
      const docMatches = (alignment.docs_matches || []).slice(0, 5).map(item => `<li><code>${escapeHtml(item.document || "")}</code> 第 ${escapeHtml(item.page || "")} 页，模块：${escapeHtml(item.module || "")}</li>`).join("");
      const improvements = (alignment.training_improvements || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const alignmentHtml = externalCases || docMatches || improvements
        ? `<h3>总知识库对齐</h3>${externalCases ? `<h3>相似 COMSOL 案例</h3><ul>${externalCases}</ul>` : ""}${docMatches ? `<h3>官方文档校对</h3><ul>${docMatches}</ul>` : ""}${improvements ? `<h3>训练完善建议</h3><ul>${improvements}</ul>` : ""}`
        : "";
      return `<h3>案例学习完成</h3><p>${escapeHtml(summary.summary || "")}</p><ul><li>训练阶段：<code>${escapeHtml(card.training_stage || "")}</code></li><li>文件数：${escapeHtml(fileSummary.count || 0)}</li><li>MATLAB：${escapeHtml(fileSummary.matlab_files || 0)}，Java：${escapeHtml(fileSummary.java_files || 0)}，PDF：${escapeHtml(fileSummary.pdf_files || 0)}，MPH：${escapeHtml(fileSummary.mph_files || 0)}，CSV：${escapeHtml(fileSummary.csv_files || 0)}</li><li>记忆库案例数：${escapeHtml(memory.case_count || 0)}</li></ul>${contentHtml}${trace ? `<h3>学习过程/判断依据</h3><ul>${trace}</ul>` : ""}${alignmentHtml}${logic ? `<h3>学到的建模逻辑</h3><ul>${logic}</ul>` : ""}${params ? `<h3>提取参数</h3><ul>${params}</ul>` : ""}${assets ? `<h3>可复用资产</h3><ul>${assets}</ul>` : ""}${next ? `<h3>下一步</h3><ul>${next}</ul>` : ""}<h3>输出文件</h3><ul><li>JSON：<code>${escapeHtml(outputs.json || "")}</code></li><li>Markdown：<code>${escapeHtml(outputs.markdown || "")}</code></li><li>Index：<code>${escapeHtml(outputs.index || "")}</code></li></ul>`;
    }

    function summarizeArticleLearningResponse(data) {
      if (!data.ok) {
        return `<h3>文章学习失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      const card = data.card || {};
      const plan = card.memory_assisted_model_plan || {};
      const params = (card.parameters || []).map(item => `<li><code>${escapeHtml(item.name)}</code> = <code>${escapeHtml(item.value || "")}</code> ${escapeHtml(item.role || "")}</li>`).join("");
      const corrections = (card.correction_strategy || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const matches = (plan.matched_cases || []).slice(0, 6).map(item => `<li><code>${escapeHtml(item.title || "")}</code> score=${escapeHtml(item.score || "")}</li>`).join("");
      const steps = (plan.recommended_modeling_steps || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const outputs = (plan.validation_outputs || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const files = data.outputs || {};
      return `<h3>文章驱动建模方案已生成</h3><p>${escapeHtml(card.summary || "")}</p><h3>文章参数</h3><ul>${params}</ul><h3>文章修正要求</h3><ul>${corrections}</ul>${matches ? `<h3>记忆库匹配案例</h3><ul>${matches}</ul>` : ""}<h3>COMSOL 建模步骤</h3><ul>${steps}</ul><h3>验证输出</h3><ul>${outputs}</ul><h3>输出文件</h3><ul><li>JSON：<code>${escapeHtml(files.json || "")}</code></li><li>Markdown：<code>${escapeHtml(files.markdown || "")}</code></li></ul>`;
    }

    function summarizePlanResponse(data) {
      if (!data.ok) {
        return `<h3>建模方案生成失败</h3><p>${escapeHtml(data.error || "未知错误")}</p>`;
      }
      const plan = data.plan || {};
      const domains = (plan.inferred_domains || []).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
      const cases = (plan.matched_cases || [])
        .map(item => `<li><code>${escapeHtml(item.title)}</code> score=${escapeHtml(item.score)}</li>`)
        .join("");
      const steps = (plan.recommended_modeling_steps || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const params = (plan.candidate_parameters || [])
        .slice(0, 12)
        .map(item => `<li><code>${escapeHtml(item.name)}</code> ${escapeHtml(item.value || "")}</li>`)
        .join("");
      const outputs = (plan.candidate_outputs || []).map(item => `<code>${escapeHtml(item)}</code>`).join(" ");
      const limitations = (plan.limitations || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const externalCases = (plan.external_case_matches || []).slice(0, 5).map(item => `<li><code>${escapeHtml(item.title || "")}</code> score=${escapeHtml(item.score || "")}</li>`).join("");
      const docMatches = (plan.official_doc_matches || []).slice(0, 5).map(item => `<li><code>${escapeHtml(item.document || "")}</code> 第 ${escapeHtml(item.page || "")} 页</li>`).join("");
      return `<h3>COMSOL 建模方案</h3><p>${domains || "<code>general_multiphysics</code>"}</p>${cases ? `<h3>本地记忆匹配案例</h3><ul>${cases}</ul>` : ""}${externalCases ? `<h3>总案例库参考</h3><ul>${externalCases}</ul>` : ""}${docMatches ? `<h3>官方文档参考</h3><ul>${docMatches}</ul>` : ""}<h3>建模步骤</h3><ul>${steps}</ul>${params ? `<h3>候选参数</h3><ul>${params}</ul>` : ""}<h3>建议输出</h3><p>${outputs}</p><h3>限制</h3><ul>${limitations}</ul>`;
    }

    async function loadDefaults() {
      const response = await fetch("/api/default-constraints");
      const data = await response.json();
      constraints.value = JSON.stringify(data, null, 2);
      renderJson(data);
      setStatus("loaded", "ok");
      addMessage("assistant", "<h3>已载入示例约束</h3><p>你可以在右侧修改参数范围、边界条件和输出表达式，然后让我校验或生成 MATLAB 脚本。</p>");
    }

    async function sendPrompt() {
      const prompt = document.getElementById("prompt");
      const text = prompt.value.trim();
      if (!text) return;
      addMessage("user", escapeHtml(text));
      prompt.value = "";
      const data = await request("/api/instruction", {instruction: text, file_summary: lastFileSummary});
      addMessage("assistant", summarizeInstructionResponse(data));
    }

    async function planModelFromPrompt() {
      const prompt = document.getElementById("prompt");
      const text = prompt.value.trim() || "根据已经学习的案例构建 COMSOL 模型，并给出建模、理论、约束和分析路径。";
      addMessage("user", escapeHtml(text));
      prompt.value = "";
      const data = await request("/api/plan-model", {requirement: text});
      addMessage("assistant", summarizePlanResponse(data));
      return data;
    }

    function useTemplate(text) {
      document.getElementById("prompt").value = text;
      document.getElementById("prompt").focus();
    }

    function selectThreadMode(mode) {
      document.querySelectorAll(".thread").forEach(button => {
        button.classList.toggle("active", button.dataset.mode === mode);
      });
      const config = {
        chat: {
          target: null,
          prompt: "请作为 COMSOL 训练助手，解释当前任务应该如何拆分为案例学习、建模、约束和训练步骤。",
          message: "<h3>当前会话</h3><p>这里用于连续对话。我会保留已读文件上下文，并把后续问题理解为 COMSOL 案例学习、自动建模或代理模型训练任务。</p>"
        },
        modeling: {
          target: "tool-constraints",
          prompt: "根据当前约束和已学习案例，生成 COMSOL 自动建模方案，并说明参数、几何、材料、物理场、网格、研究和结果导出顺序。",
          message: "<h3>自动建模</h3><p>这个模式会优先使用右侧约束 JSON、本地案例记忆和 LiveLink MATLAB 生成能力。适合让模型给出建模方案或生成 MATLAB 建模脚本。</p>"
        },
        reading: {
          target: "tool-files",
          prompt: "请读取右侧多个文件，并总结它们对 COMSOL 建模理论、参数约束、案例学习和后续训练的作用。",
          message: "<h3>文件阅读</h3><p>这个模式对应右侧文件工具。可以一次读取 MATLAB、Java、PDF、MPH、CSV、JSON 等文件，并生成学习总结。</p>"
        },
        training: {
          target: "tool-training",
          prompt: "根据 CSV 数据训练 COMSOL 代理模型，对比候选模型，输出 RMSE、MAE、R2、样本预测和后续改进建议。",
          message: "<h3>代理模型训练</h3><p>这个模式对应右侧训练工具。需要 CSV 参数扫描数据；没有 CSV 时，应先从案例学习和 COMSOL 参数扫描开始。</p>"
        }
      }[mode];
      if (!config) return;
      useTemplate(config.prompt);
      if (config.target) {
        document.getElementById(config.target)?.scrollIntoView({behavior: "smooth", block: "start"});
      }
      addMessage("assistant", config.message);
    }

    function clearChat() {
      messages.innerHTML = "";
      addWelcome();
    }

    function addWelcome() {
      addMessage("assistant", "<h3>你好，我是 COMSOL 训练对话助手。</h3><p>你可以像和 Codex 对话一样描述任务。我会围绕 COMSOL 案例学习、理论总结、约束整理、LiveLink MATLAB 建模和代理模型训练给出解释、判断依据和下一步操作。</p><p>如果你先读取多个案例文件，我会把当前文件上下文带入后续对话；如果本地案例记忆里有相似案例，我也会主动引用。</p>");
    }

    function initializeCaseFieldSync() {
      syncCaseTitleFromCaseDir();
    }

    async function inspectMatlab() {
      const data = await request("/api/inspect-matlab", {path: document.getElementById("matlabPath").value});
      addMessage("assistant", summarizeGeneric("MATLAB 解析", data));
      return data;
    }

    function splitPathList(value) {
      return String(value || "")
        .split(/\r?\n|;/)
        .map(item => item.trim())
        .filter(Boolean);
    }

    function normalizePathForUi(path) {
      return String(path || "").replaceAll("\\", "/").replace(/\/+$/, "");
    }

    function pathLooksLikeFile(path) {
      const name = normalizePathForUi(path).split("/").pop() || "";
      return /\.[A-Za-z0-9]{1,8}$/.test(name);
    }

    function parentDirectory(path) {
      const normalized = normalizePathForUi(path);
      if (!normalized) return "";
      const parts = normalized.split("/");
      if (pathLooksLikeFile(normalized)) {
        parts.pop();
      }
      return parts.join("/");
    }

    function commonDirectory(paths) {
      const dirs = paths.map(parentDirectory).filter(Boolean);
      if (!dirs.length) return "";
      const splitDirs = dirs.map(dir => dir.split("/"));
      const common = [];
      for (let index = 0; index < splitDirs[0].length; index += 1) {
        const part = splitDirs[0][index];
        if (splitDirs.every(items => items[index] === part)) {
          common.push(part);
        } else {
          break;
        }
      }
      return common.join("/");
    }

    function baseName(path) {
      const normalized = normalizePathForUi(path);
      return normalized.split("/").filter(Boolean).pop() || "";
    }

    function stripExtension(name) {
      return String(name || "").replace(/\.[A-Za-z0-9]{1,8}$/, "");
    }

    function caseTitleFromPath(path) {
      const name = stripExtension(baseName(path));
      return name.replace(/[^\p{L}\p{N}_-]+/gu, "_").replace(/^_+|_+$/g, "") || "comsol_case";
    }

    function setCaseFields(caseDir, caseTitle) {
      const caseDirInput = document.getElementById("caseDir");
      const caseTitleInput = document.getElementById("caseTitle");
      if (caseDir) caseDirInput.value = caseDir;
      if (caseTitle) caseTitleInput.value = caseTitle;
    }

    function setInputValue(id, value) {
      const input = document.getElementById(id);
      if (input && value) input.value = value;
    }

    function extensionOf(path) {
      const name = baseName(path).toLowerCase();
      const match = name.match(/(\.[a-z0-9]+)$/);
      return match ? match[1] : "";
    }

    function firstPathByExtension(paths, extensions) {
      const wanted = new Set(extensions);
      return paths.find(path => wanted.has(extensionOf(path))) || "";
    }

    function setCaseSyncInfo(parts) {
      const info = document.getElementById("caseSyncInfo");
      if (info) info.value = parts.filter(Boolean).join("；") || "等待选择文件或输入路径";
    }

    function syncCaseTitleFromCaseDir() {
      const dir = normalizePathForUi(document.getElementById("caseDir").value);
      if (!dir) return;
      const caseTitle = caseTitleFromPath(dir);
      setCaseFields(dir, caseTitle);
      setInputValue("modelName", `${caseTitle}_surrogate.joblib`);
      setCaseSyncInfo([`案例目录已关联：${dir}`, `案例名称：${caseTitle}`]);
    }

    function syncRelatedFieldsFromPaths(paths) {
      if (!paths.length) return;
      const dir = paths.length > 1 ? commonDirectory(paths) : parentDirectory(paths[0]);
      const titleSource = dir || parentDirectory(paths[0]) || paths[0];
      const caseTitle = caseTitleFromPath(titleSource);
      const matlabPath = firstPathByExtension(paths, [".m"]);
      const csvPath = firstPathByExtension(paths, [".csv"]);
      setCaseFields(dir, caseTitle);
      setInputValue("matlabPath", matlabPath);
      setInputValue("csvPath", csvPath);
      setInputValue("modelName", `${caseTitle}_surrogate.joblib`);
      setCaseSyncInfo([
        dir ? `案例目录已关联：${dir}` : "",
        matlabPath ? `MATLAB：${baseName(matlabPath)}` : "",
        csvPath ? `CSV：${baseName(csvPath)}` : "",
        `模型文件：${caseTitle}_surrogate.joblib`,
      ]);
    }

    function syncTrainingColumnsFromSummary(summary) {
      const csvSummary = findCsvSummary(summary);
      const columns = csvSummary?.details?.columns || [];
      if (!columns.length) return;
      const outputKeywords = /(out|output|result|target|tmax|tavg|temp|temperature|stress|strain|disp|pressure|velocity|flux|current|voltage|loss|power|force|volume|area|error|max|min|avg)/i;
      const outputs = columns.filter(name => outputKeywords.test(String(name)));
      const inputs = columns.filter(name => !outputs.includes(name));
      if (inputs.length) setInputValue("inputs", inputs.join(" "));
      if (outputs.length) setInputValue("outputs", outputs.join(" "));
      setCaseSyncInfo([
        document.getElementById("caseSyncInfo")?.value || "",
        `训练列已关联：输入 ${inputs.length || 0} 个，输出 ${outputs.length || 0} 个`,
      ]);
    }

    function findCsvSummary(summary) {
      if (!summary) return null;
      if (summary.kind === "csv_table") return summary;
      if (summary.kind === "file_collection") {
        return (summary.files || []).find(file => file.kind === "csv_table") || null;
      }
      return null;
    }

    function syncCaseFieldsFromPaths() {
      const paths = splitPathList(document.getElementById("filePath").value);
      if (!paths.length) return;
      syncRelatedFieldsFromPaths(paths);
    }

    function syncCaseFieldsFromUpload() {
      const files = Array.from(document.getElementById("uploadFile").files || []);
      if (!files.length) return;
      const relativePaths = files
        .map(file => file.webkitRelativePath || "")
        .filter(Boolean);
      if (relativePaths.length) {
        const dir = relativePaths.length > 1 ? commonDirectory(relativePaths) : parentDirectory(relativePaths[0]);
        syncRelatedFieldsFromPaths(relativePaths);
        return;
      }
      const names = files.map(file => file.name || "").filter(Boolean);
      const firstName = names[0] || "comsol_case";
      const caseTitle = caseTitleFromPath(firstName);
      setCaseFields("", caseTitle);
      setInputValue("matlabPath", firstPathByExtension(names, [".m"]));
      setInputValue("csvPath", firstPathByExtension(names, [".csv"]));
      setInputValue("modelName", `${caseTitle}_surrogate.joblib`);
      setCaseSyncInfo([
        `已选择 ${files.length} 个上传文件`,
        firstPathByExtension(names, [".m"]) ? `MATLAB：${firstPathByExtension(names, [".m"])}` : "",
        firstPathByExtension(names, [".csv"]) ? `CSV：${firstPathByExtension(names, [".csv"])}` : "",
      ]);
    }

    async function readFilePath() {
      syncCaseFieldsFromPaths();
      const paths = splitPathList(document.getElementById("filePath").value);
      const endpoint = paths.length > 1 ? "/api/read-files" : "/api/read-file";
      const body = paths.length > 1 ? {paths} : {path: paths[0] || ""};
      const data = await request(endpoint, body);
      if (data.ok) {
        lastFileSummary = data.summary;
        syncTrainingColumnsFromSummary(lastFileSummary);
      }
      addMessage("assistant", summarizeFileResponse(data));
      return data;
    }

    async function readUploadedFile() {
      syncCaseFieldsFromUpload();
      const files = Array.from(document.getElementById("uploadFile").files);
      if (!files.length) {
        const data = {ok: false, error: "No file selected"};
        renderJson(data);
        setStatus("failed", "bad");
        addMessage("assistant", summarizeFileResponse(data));
        return;
      }
      const payloadFiles = [];
      for (const file of files) {
        payloadFiles.push({name: file.name, content: await file.text()});
      }
      const endpoint = payloadFiles.length > 1 ? "/api/read-uploaded-files" : "/api/read-uploaded-file";
      const body = payloadFiles.length > 1 ? {files: payloadFiles} : payloadFiles[0];
      const data = await request(endpoint, body);
      if (data.ok) {
        lastFileSummary = data.summary;
        syncTrainingColumnsFromSummary(lastFileSummary);
      }
      addMessage("assistant", summarizeFileResponse(data));
      return data;
    }

    async function buildLearningSummary() {
      if (!lastFileSummary) {
        const data = {ok: false, error: "No file summary available. Read one or more files first."};
        renderJson(data);
        setStatus("failed", "bad");
        addMessage("assistant", summarizeLearningResponse(data));
        return data;
      }
      const data = await request("/api/learning-summary", {file_summary: lastFileSummary});
      addMessage("assistant", summarizeLearningResponse(data));
      return data;
    }

    async function learnCaseDirectory() {
      syncCaseTitleFromCaseDir();
      const data = await request("/api/learn-case", {
        case_dir: document.getElementById("caseDir").value,
        title: document.getElementById("caseTitle").value
      });
      addMessage("assistant", summarizeCaseLearningResponse(data));
      return data;
    }

    async function learnArticleDocument() {
      const data = await request("/api/learn-article", {
        article_path: document.getElementById("articlePath").value
      });
      addMessage("assistant", summarizeArticleLearningResponse(data));
      return data;
    }

    async function validateConstraints() {
      const data = await request("/api/validate-constraints", {constraints_json: constraints.value});
      addMessage("assistant", data.ok ? "<h3>约束校验通过</h3><p>当前 JSON 可以用于生成 COMSOL LiveLink MATLAB 脚本。</p>" : summarizeGeneric("约束校验", data));
      return data;
    }

    async function generateMatlab() {
      let name = "generated_build_thermal_rectangle_surrogate.m";
      try {
        const cfg = JSON.parse(constraints.value);
        name = "generated_build_" + cfg.model_name + ".m";
      } catch (err) {}
      const data = await request("/api/generate-matlab", {constraints_json: constraints.value, output_name: name});
      const html = data.ok
        ? `<h3>MATLAB 脚本已生成</h3><p>路径：<code>${escapeHtml(data.path)}</code></p>`
        : summarizeGeneric("MATLAB 生成", data);
      addMessage("assistant", html);
      return data;
    }

    async function generateComsolCode() {
      const requirement = document.getElementById("codeRequirement").value || document.getElementById("prompt").value;
      const title = caseTitleFromPath(document.getElementById("caseTitle").value || "generated_comsol_model");
      const data = await request("/api/generate-comsol-code", {
        requirement,
        output_prefix: title || "generated_comsol_model",
        existing_content: document.getElementById("existingComsolContent").value
      });
      addMessage("assistant", summarizeComsolCodeResponse(data));
      return data;
    }

    async function trainModel() {
      const data = await request("/api/train", {
        csv_path: document.getElementById("csvPath").value,
        input_columns: document.getElementById("inputs").value,
        output_columns: document.getElementById("outputs").value,
        model_name: document.getElementById("modelName").value
      });
      const report = data.report || {};
      const candidateRows = (report.candidate_reports || [])
        .map(item => `<li><code>${escapeHtml(item.name)}</code> RMSE=${escapeHtml(item.test_rmse)} R2=${escapeHtml(item.test_r2)}</li>`)
        .join("");
      const summaryRows = (report.training_summary || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const recommendationRows = (report.recommendations || []).map(item => `<li>${escapeHtml(item)}</li>`).join("");
      const html = data.ok
        ? `<h3>训练完成</h3><p>模型：<code>${escapeHtml(data.model_path)}</code></p><p>最佳候选：<code>${escapeHtml(report.best_model)}</code></p><p>测试 RMSE：<code>${escapeHtml(report.test_rmse)}</code>，MAE：<code>${escapeHtml(report.test_mae)}</code>，R2：<code>${escapeHtml(report.test_r2)}</code></p>${summaryRows ? `<h3>训练总结</h3><ul>${summaryRows}</ul>` : ""}${candidateRows ? `<h3>候选模型对比</h3><ul>${candidateRows}</ul>` : ""}${recommendationRows ? `<h3>后续建议</h3><ul>${recommendationRows}</ul>` : ""}`
        : summarizeGeneric("训练", data);
      addMessage("assistant", html);
      return data;
    }

    document.getElementById("prompt").addEventListener("keydown", event => {
      if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
        event.preventDefault();
        sendPrompt();
      }
    });

    addWelcome();
    initializeCaseFieldSync();
    loadDefaults();
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    run(host=args.host, port=args.port, open_browser=args.open)
