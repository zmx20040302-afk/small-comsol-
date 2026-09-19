from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import webbrowser
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from comsol_small_model.comsol_server import ensure_comsol_server  # noqa: E402


def _healthy_port(start_port: int, span: int = 20) -> int | None:
    for port in range(start_port, start_port + span):
        try:
            with urlopen(f"http://127.0.0.1:{port}/api/health", timeout=1.0) as response:
                if response.status == 200:
                    return port
        except OSError:
            continue
    return None


def _worker_is_online(root: Path) -> bool:
    status_path = root / "generated" / "execution_jobs" / "worker_status.json"
    if not status_path.is_file():
        return False
    try:
        status = json.loads(status_path.read_text(encoding="utf-8"))
        updated_at = datetime.fromisoformat(str(status.get("updated_at", "")).replace("Z", "+00:00"))
        age = (datetime.now(timezone.utc) - updated_at).total_seconds()
        return status.get("state") == "running" and 0 <= age <= 15
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return False


def _start_worker(root: Path) -> dict[str, object]:
    if _worker_is_online(root):
        return {"started": False, "online": True, "message": "COMSOL execution worker 已在运行。"}
    log_path = root / "generated" / "execution_jobs" / "worker_startup.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as log:
        flags = (
            getattr(subprocess, "DETACHED_PROCESS", 0x00000008)
            | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
        )
        kwargs: dict[str, object] = {
            "cwd": root,
            "stdin": subprocess.DEVNULL,
            "stdout": log,
            "stderr": subprocess.STDOUT,
            "close_fds": True,
        }
        if sys.platform == "win32":
            kwargs["creationflags"] = flags
        else:
            kwargs["start_new_session"] = True
        process = subprocess.Popen(
            [sys.executable, str(root / "execution_worker.py"), "--poll-seconds", "5"],
            **kwargs,
        )
    return {"started": True, "online": False, "pid": process.pid, "log_path": str(log_path)}


def _ensure_startup_server(root: Path) -> dict[str, object]:
    config_path = root / "configs" / "execution_node.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ready": False, "message": f"无法读取 COMSOL 执行配置：{exc}"}
    log_path = (
        root
        / "generated"
        / "training_runs"
        / f"comsol_mphserver_startup_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    )
    return ensure_comsol_server(config, log_path=log_path, detached=True)


def _browser_url(host: str, port: int) -> str:
    browser_host = "127.0.0.1" if host in {"0.0.0.0", "::"} else host
    return f"http://{browser_host}:{port}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Start the COMSOL small model web service detached on Windows")
    parser.add_argument("--port", type=int, default=8880)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--wait-seconds", type=float, default=15.0)
    parser.add_argument("--open", action="store_true", help="Open the ready local service in the default browser.")
    parser.add_argument("--with-worker", action="store_true", help="Start the single-instance local execution worker.")
    parser.add_argument("--worker-only", action="store_true", help="Start only the local execution worker.")
    parser.add_argument(
        "--ensure-comsol-server",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Check and start COMSOL mphserver; defaults to enabled with --with-worker.",
    )
    args = parser.parse_args()
    root = ROOT
    web_app = root / "web_app.py"
    run_worker = bool(args.with_worker or args.worker_only)
    ensure_server = run_worker if args.ensure_comsol_server is None else bool(args.ensure_comsol_server)
    if ensure_server:
        server = _ensure_startup_server(root)
        if server.get("ready"):
            print(f"comsol_server_ready=true host={server.get('host')} port={server.get('port')}")
        else:
            print(f"comsol_server_ready=false message={server.get('message', '')}")
    if run_worker:
        worker = _start_worker(root)
        print(
            f"worker_started={str(bool(worker.get('started'))).lower()} "
            f"worker_online={str(bool(worker.get('online'))).lower()} "
            f"worker_pid={worker.get('pid', '')}"
        )
    if args.worker_only:
        return
    existing_port = _healthy_port(args.port, span=1)
    if existing_port is not None:
        print(f"reused=true port={existing_port} ready=true")
        if args.open:
            webbrowser.open(_browser_url(args.host, existing_port))
        return
    flags = getattr(subprocess, "DETACHED_PROCESS", 0x00000008) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
    web_kwargs: dict[str, object] = {
        "cwd": root,
        "stdin": subprocess.DEVNULL,
        "stdout": subprocess.DEVNULL,
        "stderr": subprocess.DEVNULL,
        "close_fds": True,
    }
    if sys.platform == "win32":
        web_kwargs["creationflags"] = flags
    else:
        web_kwargs["start_new_session"] = True
    process = subprocess.Popen(
        [sys.executable, str(web_app), "--host", args.host, "--port", str(args.port)],
        **web_kwargs,
    )
    deadline = time.monotonic() + args.wait_seconds
    while time.monotonic() < deadline:
        active_port = _healthy_port(args.port)
        if active_port is not None:
            print(f"started_pid={process.pid} port={active_port} ready=true")
            if args.open:
                webbrowser.open(_browser_url(args.host, active_port))
            return
        time.sleep(0.5)
    if process.poll() is None:
        print(f"started_pid={process.pid} port={args.port} ready=pending url={_browser_url(args.host, args.port)}")
        return
    raise RuntimeError(f"service process exited before becoming ready (exit={process.returncode})")


if __name__ == "__main__":
    main()
