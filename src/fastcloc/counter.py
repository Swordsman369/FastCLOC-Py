from __future__ import annotations

import time
from pathlib import Path
from .comments import count_lines
from .detector import detect_language
from .models import FileRecord, LanguageSpec, ScanConfig, ScanSummary
from .scanner import iter_source_paths
from .security import file_digest, inspect_file

_TEXT_SPEC = LanguageSpec(name="Text", extensions=(), line_comments=(), block_comments=())


def read_text_lines(path: Path, config: ScanConfig) -> list[str]:
    text = path.read_text(encoding=config.encoding, errors=config.errors)
    if text and not text.endswith("\n"):
        return text.splitlines()
    return text.splitlines()


def count_text(text: str, spec: LanguageSpec) -> tuple[int, int, int]:
    return count_lines(text.splitlines(), spec)


def count_file(path: Path, config: ScanConfig) -> FileRecord:
    allowed, reason, size = inspect_file(path, config)
    if not allowed:
        return FileRecord(path=str(path), language="Ignored", ignored=True, reason=reason, size_bytes=size)
    try:
        lines = read_text_lines(path, config)
    except OSError as exc:
        return FileRecord(path=str(path), language="Ignored", ignored=True, reason=f"read failed: {exc}", size_bytes=size)
    first_line = lines[0] if lines else ""
    spec = detect_language(path, config=config, first_line=first_line) or _TEXT_SPEC
    blank, comment, code = count_lines(lines, spec)
    digest = ""
    try:
        digest = file_digest(path)
    except OSError:
        digest = ""
    return FileRecord(
        path=str(path),
        language=spec.name,
        blank=blank,
        comment=comment,
        code=code,
        total=len(lines),
        size_bytes=size,
        digest=digest,
    )


def count_path(root: Path, config: ScanConfig | None = None) -> ScanSummary:
    config = config or ScanConfig()
    start = time.perf_counter()
    summary = ScanSummary(root=str(root))
    for path in iter_source_paths(root, config):
        summary.add_record(count_file(path, config))
    summary.elapsed_seconds = time.perf_counter() - start
    return summary
