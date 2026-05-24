from __future__ import annotations

from pathlib import Path
from .counter import count_path, count_text
from .diff import compare_paths as _compare_paths
from .detector import detect_language
from .languages import get_language_spec
from .models import LanguageSpec, ScanConfig, ScanSummary


def analyze_path(path: str | Path, config: ScanConfig | None = None) -> ScanSummary:
    return count_path(Path(path), config=config)


def analyze_text(text: str, language: str) -> dict[str, int | str]:
    spec = get_language_spec(language) or LanguageSpec(name=language)
    blank, comment, code = count_text(text, spec)
    return {"language": spec.name, "blank": blank, "comment": comment, "code": code, "total": blank + comment + code}


def compare_paths(old_path: str | Path, new_path: str | Path, config: ScanConfig | None = None):
    return _compare_paths(old_path, new_path, config=config)


def detect_path_language(path: str | Path, config: ScanConfig | None = None) -> str:
    spec = detect_language(Path(path), config=config)
    return spec.name if spec else "Text"
