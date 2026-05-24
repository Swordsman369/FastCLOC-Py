from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from .counter import count_path
from .models import ScanConfig, ScanSummary


@dataclass
class ProjectHealth:
    root: str
    source_files: int
    ignored_files: int
    code_lines: int
    comment_lines: int
    blank_lines: int
    comment_ratio: float
    largest_language: str

    def to_dict(self) -> dict[str, int | float | str]:
        return {
            "root": self.root,
            "source_files": self.source_files,
            "ignored_files": self.ignored_files,
            "code_lines": self.code_lines,
            "comment_lines": self.comment_lines,
            "blank_lines": self.blank_lines,
            "comment_ratio": self.comment_ratio,
            "largest_language": self.largest_language,
        }


def summarize_project(summary: ScanSummary) -> ProjectHealth:
    totals = summary.sorted_totals()
    largest = totals[0].language if totals else "None"
    denominator = max(summary.total_code + summary.total_comment, 1)
    return ProjectHealth(
        root=summary.root,
        source_files=summary.total_files,
        ignored_files=summary.total_ignored,
        code_lines=summary.total_code,
        comment_lines=summary.total_comment,
        blank_lines=summary.total_blank,
        comment_ratio=summary.total_comment / denominator,
        largest_language=largest,
    )


def analyze_project_health(path: str | Path, config: ScanConfig | None = None) -> ProjectHealth:
    return summarize_project(count_path(Path(path), config=config))


def enforce_minimum_code_lines(path: str | Path, minimum: int = 2000, config: ScanConfig | None = None) -> tuple[bool, ProjectHealth]:
    health = analyze_project_health(path, config=config)
    return health.code_lines >= minimum, health
