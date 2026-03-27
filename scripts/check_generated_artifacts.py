from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description="Falha se caminhos gerados ficaram sujos após regeneração.")
    parser.add_argument("paths", nargs="+", help="Caminhos a verificar.")
    args = parser.parse_args()

    changed = run_git("status", "--porcelain", "--", *args.paths).splitlines()
    if changed:
        print("Artefatos gerados ficaram divergentes após a regeneração:", file=sys.stderr)
        for line in changed:
            print(f"- {line}", file=sys.stderr)
        return 1

    print("Artefatos gerados estão sincronizados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
