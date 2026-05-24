from __future__ import annotations

import csv
import io
import json
from .models import LanguageTotal, ScanSummary


def _summary_rows(summary: ScanSummary) -> list[LanguageTotal]:
    return summary.sorted_totals()


def render_table(summary: ScanSummary) -> str:
    rows = _summary_rows(summary)
    widths = {
        "language": max([8] + [len(item.language) for item in rows] + [3]),
        "files": 7,
        "blank": 8,
        "comment": 9,
        "code": 8,
    }
    parts = []
    header = f"{'Language':<{widths['language']}} {'files':>{widths['files']}} {'blank':>{widths['blank']}} {'comment':>{widths['comment']}} {'code':>{widths['code']}}"
    parts.append(header)
    parts.append("-" * len(header))
    for item in rows:
        parts.append(f"{item.language:<{widths['language']}} {item.files:>{widths['files']}} {item.blank:>{widths['blank']}} {item.comment:>{widths['comment']}} {item.code:>{widths['code']}}")
    parts.append("-" * len(header))
    parts.append(f"{'SUM':<{widths['language']}} {summary.total_files:>{widths['files']}} {summary.total_blank:>{widths['blank']}} {summary.total_comment:>{widths['comment']}} {summary.total_code:>{widths['code']}}")
    parts.append(f"Ignored files: {summary.total_ignored}; elapsed: {summary.elapsed_seconds:.4f}s")
    return "\n".join(parts)


def render_json(summary: ScanSummary, by_file: bool = False) -> str:
    return json.dumps(summary.to_dict(by_file=by_file), indent=2, ensure_ascii=False, sort_keys=True)


def render_csv(summary: ScanSummary, by_file: bool = False) -> str:
    output = io.StringIO()
    if by_file:
        fields = ["path", "language", "blank", "comment", "code", "total", "size_bytes", "digest"]
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for record in sorted(summary.files, key=lambda item: item.path):
            row = record.to_dict()
            writer.writerow({field: row[field] for field in fields})
    else:
        fields = ["language", "files", "blank", "comment", "code", "total"]
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for row in summary.sorted_totals():
            writer.writerow(row.to_dict())
    return output.getvalue()


def render_markdown(summary: ScanSummary) -> str:
    parts = ["| Language | Files | Blank | Comment | Code |", "|---|---:|---:|---:|---:|"]
    for item in summary.sorted_totals():
        parts.append(f"| {item.language} | {item.files} | {item.blank} | {item.comment} | {item.code} |")
    parts.append(f"| **SUM** | **{summary.total_files}** | **{summary.total_blank}** | **{summary.total_comment}** | **{summary.total_code}** |")
    return "\n".join(parts)


def render_report(summary: ScanSummary, fmt: str, by_file: bool = False) -> str:
    normalized = fmt.lower()
    if normalized == "table":
        return render_table(summary)
    if normalized == "json":
        return render_json(summary, by_file=by_file)
    if normalized == "csv":
        return render_csv(summary, by_file=by_file)
    if normalized == "markdown":
        return render_markdown(summary)
    raise ValueError(f"unsupported report format: {fmt}")
