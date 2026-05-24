from __future__ import annotations

from pathlib import Path
from typing import Iterable


def normalize_path(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def chunked(items: list[str], size: int) -> list[list[str]]:
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[index:index + size] for index in range(0, len(items), size)]


def plural(count: int, singular: str, plural_word: str | None = None) -> str:
    if count == 1:
        return f"1 {singular}"
    return f"{count} {plural_word or singular + 's'}"


def read_list_file(path: str | Path) -> tuple[str, ...]:
    p = Path(path)
    if not p.exists():
        return ()
    values: list[str] = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            values.append(stripped)
    return tuple(values)


def stable_relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except (OSError, ValueError):
        return str(path)


def coerce_extensions(values: Iterable[str]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            continue
        ext, language = item.split("=", 1)
        ext = ext.strip().lower().lstrip(".")
        language = language.strip()
        if ext and language:
            mapping[ext] = language
    return mapping
