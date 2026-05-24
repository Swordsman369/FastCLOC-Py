from __future__ import annotations

from pathlib import Path
from collections.abc import Iterator
from .models import ScanConfig


def iter_source_paths(root: Path, config: ScanConfig) -> Iterator[Path]:
    if root.is_file():
        yield root
        return
    if not root.exists():
        return
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            children = sorted(current.iterdir(), key=lambda item: item.name.lower())
        except OSError:
            continue
        for child in children:
            if child.is_dir():
                if child.is_symlink() and not config.follow_symlinks:
                    continue
                if config.should_ignore_dir(child):
                    continue
                stack.append(child)
            elif child.is_file() or child.is_symlink():
                yield child


def collect_source_paths(root: Path, config: ScanConfig) -> list[Path]:
    return list(iter_source_paths(root, config))
