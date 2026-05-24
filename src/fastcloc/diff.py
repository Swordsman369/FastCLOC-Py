from __future__ import annotations

from pathlib import Path
from .counter import count_path
from .models import DiffRecord, ScanConfig, ScanSummary


def diff_summaries(old: ScanSummary, new: ScanSummary) -> list[DiffRecord]:
    old_totals = old.totals_by_language
    new_totals = new.totals_by_language
    languages = sorted(set(old_totals) | set(new_totals))
    rows: list[DiffRecord] = []
    for language in languages:
        old_row = old_totals.get(language)
        new_row = new_totals.get(language)
        rows.append(
            DiffRecord(
                language=language,
                old_code=old_row.code if old_row else 0,
                new_code=new_row.code if new_row else 0,
                old_comment=old_row.comment if old_row else 0,
                new_comment=new_row.comment if new_row else 0,
                old_blank=old_row.blank if old_row else 0,
                new_blank=new_row.blank if new_row else 0,
            )
        )
    return sorted(rows, key=lambda item: (-abs(item.delta_code), item.language.lower()))


def compare_paths(old_path: str | Path, new_path: str | Path, config: ScanConfig | None = None) -> list[DiffRecord]:
    old_summary = count_path(Path(old_path), config=config)
    new_summary = count_path(Path(new_path), config=config)
    return diff_summaries(old_summary, new_summary)


def render_diff_table(rows: list[DiffRecord]) -> str:
    widths = {"language": max([8] + [len(row.language) for row in rows]), "code": 10}
    header = f"{'Language':<{widths['language']}} {'old_code':>{widths['code']}} {'new_code':>{widths['code']}} {'delta':>{widths['code']}}"
    parts = [header, "-" * len(header)]
    for row in rows:
        parts.append(f"{row.language:<{widths['language']}} {row.old_code:>{widths['code']}} {row.new_code:>{widths['code']}} {row.delta_code:>{widths['code']}}")
    return "\n".join(parts)
