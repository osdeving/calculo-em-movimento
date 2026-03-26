from __future__ import annotations

import json
import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "renderers" / "mdbook"
STATE_DIR = ROOT / ".tmp"
STATE_FILE = STATE_DIR / "mdbook-serve.json"
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 3000


def is_port_free(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock.connect_ex((host, port)) != 0


def pid_is_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def load_state() -> dict | None:
    if not STATE_FILE.exists():
        return None
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return None


def save_state(pid: int, host: str, port: int) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"pid": pid, "host": host, "port": port}), encoding="utf-8")


def clear_state() -> None:
    if STATE_FILE.exists():
        STATE_FILE.unlink()


def terminate_pid(pid: int, label: str) -> None:
    if not pid_is_alive(pid):
        return

    print(f"[serve] encerrando {label} (pid {pid})...")
    os.kill(pid, signal.SIGTERM)
    for _ in range(30):
        if not pid_is_alive(pid):
            return
        time.sleep(0.1)

    print(f"[serve] forçando parada de {label} (pid {pid})...")
    os.kill(pid, signal.SIGKILL)


def find_project_mdbook_pids() -> list[int]:
    result = subprocess.run(
        ["ps", "-eo", "pid=,args="],
        cwd=str(ROOT),
        check=True,
        capture_output=True,
        text=True,
    )

    pids: list[int] = []
    expected_fragment = str(BOOK_DIR)
    for raw_line in result.stdout.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        pid_text, _, args = line.partition(" ")
        if not pid_text.isdigit():
            continue

        pid = int(pid_text)
        if pid == os.getpid():
            continue

        if "mdbook serve" in args and expected_fragment in args:
            pids.append(pid)

    return pids


def stop_previous() -> None:
    state = load_state()
    if not state:
        state = {}

    known_pids = set(find_project_mdbook_pids())
    pid = int(state.get("pid", 0) or 0)
    if pid > 0:
        known_pids.add(pid)

    for old_pid in sorted(known_pids):
        if pid_is_alive(old_pid):
            terminate_pid(old_pid, "instância anterior do mdBook")

    clear_state()


def find_available_port(host: str, requested_port: int) -> tuple[int, bool]:
    if is_port_free(host, requested_port):
        return requested_port, False

    port = requested_port + 1
    while port < requested_port + 100:
        if is_port_free(host, port):
            return port, True
        port += 1

    raise RuntimeError("não encontrei porta livre para o mdBook")


def serve() -> int:
    host = os.environ.get("HOST", DEFAULT_HOST)
    requested_port = int(os.environ.get("PORT", str(DEFAULT_PORT)))

    stop_previous()
    port, changed = find_available_port(host, requested_port)

    if changed:
        print(f"[serve] porta {requested_port} ocupada; usando {port} em vez disso.")

    command = ["mdbook", "serve", str(BOOK_DIR), "-n", host, "-p", str(port)]
    process = subprocess.Popen(command, cwd=str(ROOT))
    save_state(process.pid, host, port)

    def forward(sig, _frame):
        if process.poll() is None:
            process.send_signal(sig)

    signal.signal(signal.SIGINT, forward)
    signal.signal(signal.SIGTERM, forward)

    print(f"[serve] URL: http://{host}:{port}")
    try:
        return process.wait()
    finally:
        clear_state()


def stop() -> int:
    state = load_state()
    known_pids = set(find_project_mdbook_pids())

    pid = 0
    host = DEFAULT_HOST
    port = DEFAULT_PORT
    if state:
        pid = int(state.get("pid", 0) or 0)
        host = state.get("host", DEFAULT_HOST)
        port = state.get("port", DEFAULT_PORT)
        if pid > 0:
            known_pids.add(pid)

    if not known_pids:
        print("[serve] nenhuma instância gerenciada encontrada.")
        clear_state()
        return 0

    for old_pid in sorted(known_pids):
        label = f"mdBook em {host}:{port}" if old_pid == pid else "mdBook órfão do projeto"
        if pid_is_alive(old_pid):
            terminate_pid(old_pid, label)

    clear_state()
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] == "--stop":
        return stop()
    return serve()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
