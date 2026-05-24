from __future__ import annotations

import sys
from pathlib import Path


def effective_loc(path: Path) -> int:
    count = 0
    for file in path.rglob("*.py"):
        if any(part in {"__pycache__", ".git", ".venv", "venv"} for part in file.parts):
            continue
        for line in file.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                continue
            count += 1
    return count


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("src")
    print(effective_loc(target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
