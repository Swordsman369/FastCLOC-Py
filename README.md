# FastCLOC-Py

FastCLOC-Py is a small, auditable Python rewrite inspired by the classic `cloc` utility. The original `cloc` project is implemented primarily in Perl and counts blank lines, comment lines, and physical source lines across many languages. This project keeps the core idea while using Python and adding stricter scanning defaults, JSON/CSV/Markdown export, optional per-file output, and reproducible test evidence.

## Core functions

- Recursively scan a file or directory.
- Detect language by extension, exact filename, or shebang.
- Count blank, comment, and code lines.
- Aggregate totals by language and optionally by file.
- Export table, JSON, CSV, and Markdown reports.
- Compare two scans and report added/removed code volume.
- Avoid unsafe traversal by default: no symlink following, binary detection, max file size limit, and ignore rules.

## Quick start

```bash
python -m pip install -e .
fastcloc . --format table
fastcloc src --format json --by-file
fastcloc tests/fixtures --format markdown
```

## Testing

```bash
python -m unittest discover -s tests -v
python tools/count_effective_loc.py src
```

## Security posture

FastCLOC-Py performs local, read-only source analysis. It does not open network connections, execute scanned files, or write outside user-selected report paths. By default it refuses large files, binary files, hidden dependency directories, and symlink traversal.

## Rewrite scope

This repository is a rewrite rather than a fork. It contains a new Python implementation of the source scanning, language detection, counting, aggregation, and reporting workflow. It does not copy the original Perl source code.
