from __future__ import annotations

import argparse
import sys
from pathlib import Path
from .counter import count_path
from .diff import compare_paths, render_diff_table
from .models import ScanConfig
from .reporters import render_report
from .utils import coerce_extensions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fastcloc", description="Count blank, comment, and source code lines.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to scan")
    parser.add_argument("--format", choices=["table", "json", "csv", "markdown"], default="table", help="Report format")
    parser.add_argument("--by-file", action="store_true", help="Include per-file results for JSON/CSV")
    parser.add_argument("--follow-symlinks", action="store_true", help="Follow symlinked files and directories")
    parser.add_argument("--include-hidden", action="store_true", help="Include dotfiles and dot directories")
    parser.add_argument("--max-file-bytes", type=int, default=2_000_000, help="Maximum file size to count")
    parser.add_argument("--extension", action="append", default=[], metavar="EXT=LANG", help="Treat extension as language")
    parser.add_argument("--diff", nargs=2, metavar=("OLD", "NEW"), help="Compare two paths")
    return parser


def make_config(args: argparse.Namespace) -> ScanConfig:
    return ScanConfig(
        follow_symlinks=args.follow_symlinks,
        include_hidden=args.include_hidden,
        max_file_bytes=args.max_file_bytes,
        extra_extensions=coerce_extensions(args.extension),
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    config = make_config(args)
    if args.diff:
        rows = compare_paths(args.diff[0], args.diff[1], config=config)
        print(render_diff_table(rows))
        return 0
    if len(args.paths) == 1:
        summary = count_path(Path(args.paths[0]), config=config)
        print(render_report(summary, args.format, by_file=args.by_file))
        return 0
    aggregate_exit = 0
    for path in args.paths:
        summary = count_path(Path(path), config=config)
        print(f"# {path}")
        print(render_report(summary, args.format, by_file=args.by_file))
    return aggregate_exit


if __name__ == "__main__":
    raise SystemExit(main())
