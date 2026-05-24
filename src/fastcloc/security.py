from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from .models import ScanConfig


def is_binary_bytes(sample: bytes) -> bool:
    if not sample:
        return False
    if b"\x00" in sample:
        return True
    text_chars = bytes(range(32, 127)) + b"\n\r\t\f\b"
    non_text = sample.translate(None, text_chars)
    return len(non_text) / max(len(sample), 1) > 0.30


def file_digest(path: Path, chunk_size: int = 65536) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def inspect_file(path: Path, config: ScanConfig) -> tuple[bool, str, int]:
    try:
        stat = path.stat()
    except OSError as exc:
        return False, f"stat failed: {exc}", 0
    if path.is_symlink() and not config.follow_symlinks:
        return False, "symlink skipped", stat.st_size
    if stat.st_size > config.max_file_bytes:
        return False, f"file too large: {stat.st_size} bytes", stat.st_size
    if config.should_ignore_file(path):
        return False, "ignored by suffix or hidden rule", stat.st_size
    try:
        with path.open("rb") as handle:
            sample = handle.read(4096)
    except OSError as exc:
        return False, f"read failed: {exc}", stat.st_size
    if is_binary_bytes(sample):
        return False, "binary file skipped", stat.st_size
    return True, "", stat.st_size


def ensure_within_root(root: Path, candidate: Path) -> bool:
    try:
        root_resolved = root.resolve()
        candidate_resolved = candidate.resolve()
        candidate_resolved.relative_to(root_resolved)
        return True
    except (OSError, ValueError):
        return False
