from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class LanguageSpec:
    name: str
    extensions: tuple[str, ...] = ()
    filenames: tuple[str, ...] = ()
    line_comments: tuple[str, ...] = ()
    block_comments: tuple[tuple[str, str], ...] = ()
    shebangs: tuple[str, ...] = ()
    aliases: tuple[str, ...] = ()
    category: str = "programming"
    supports_strings: bool = True
    default_tab_width: int = 4

    def matches_extension(self, suffix: str) -> bool:
        token = suffix.lower().lstrip(".")
        return token in {item.lower().lstrip(".") for item in self.extensions}

    def matches_filename(self, name: str) -> bool:
        folded = name.lower()
        return folded in {item.lower() for item in self.filenames}

    def matches_shebang(self, first_line: str) -> bool:
        lowered = first_line.lower()
        return any(marker.lower() in lowered for marker in self.shebangs)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "extensions": list(self.extensions),
            "filenames": list(self.filenames),
            "line_comments": list(self.line_comments),
            "block_comments": [list(pair) for pair in self.block_comments],
            "shebangs": list(self.shebangs),
            "aliases": list(self.aliases),
            "category": self.category,
            "supports_strings": self.supports_strings,
            "default_tab_width": self.default_tab_width,
        }


@dataclass
class FileRecord:
    path: str
    language: str
    blank: int = 0
    comment: int = 0
    code: int = 0
    total: int = 0
    size_bytes: int = 0
    digest: str = ""
    ignored: bool = False
    reason: str = ""

    @property
    def counted(self) -> bool:
        return not self.ignored

    @property
    def physical(self) -> int:
        return self.blank + self.comment + self.code

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "language": self.language,
            "blank": self.blank,
            "comment": self.comment,
            "code": self.code,
            "total": self.total,
            "size_bytes": self.size_bytes,
            "digest": self.digest,
            "ignored": self.ignored,
            "reason": self.reason,
        }


@dataclass
class LanguageTotal:
    language: str
    files: int = 0
    blank: int = 0
    comment: int = 0
    code: int = 0

    @property
    def total(self) -> int:
        return self.blank + self.comment + self.code

    def add_file(self, record: FileRecord) -> None:
        if record.ignored:
            return
        self.files += 1
        self.blank += record.blank
        self.comment += record.comment
        self.code += record.code

    def merge(self, other: "LanguageTotal") -> None:
        self.files += other.files
        self.blank += other.blank
        self.comment += other.comment
        self.code += other.code

    def to_dict(self) -> dict[str, int | str]:
        return {
            "language": self.language,
            "files": self.files,
            "blank": self.blank,
            "comment": self.comment,
            "code": self.code,
            "total": self.total,
        }


@dataclass
class ScanConfig:
    follow_symlinks: bool = False
    include_hidden: bool = False
    max_file_bytes: int = 2_000_000
    encoding: str = "utf-8"
    errors: str = "replace"
    ignore_dirs: tuple[str, ...] = (
        ".git",
        ".hg",
        ".svn",
        "node_modules",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        "dist",
        "build",
        "target",
        "vendor",
        ".venv",
        "venv",
    )
    ignore_suffixes: tuple[str, ...] = (
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".webp",
        ".pdf",
        ".zip",
        ".tar",
        ".gz",
        ".bz2",
        ".xz",
        ".7z",
        ".so",
        ".dll",
        ".exe",
        ".bin",
        ".class",
        ".pyc",
    )
    extra_extensions: dict[str, str] = field(default_factory=dict)

    def should_ignore_dir(self, path: Path) -> bool:
        if not self.include_hidden and path.name.startswith("."):
            return True
        return path.name in self.ignore_dirs

    def should_ignore_file(self, path: Path) -> bool:
        if not self.include_hidden and path.name.startswith("."):
            return True
        return path.suffix.lower() in self.ignore_suffixes

    def to_dict(self) -> dict[str, Any]:
        return {
            "follow_symlinks": self.follow_symlinks,
            "include_hidden": self.include_hidden,
            "max_file_bytes": self.max_file_bytes,
            "encoding": self.encoding,
            "errors": self.errors,
            "ignore_dirs": list(self.ignore_dirs),
            "ignore_suffixes": list(self.ignore_suffixes),
            "extra_extensions": dict(self.extra_extensions),
        }


@dataclass
class ScanSummary:
    root: str
    files: list[FileRecord] = field(default_factory=list)
    ignored_files: list[FileRecord] = field(default_factory=list)
    elapsed_seconds: float = 0.0

    def add_record(self, record: FileRecord) -> None:
        if record.ignored:
            self.ignored_files.append(record)
        else:
            self.files.append(record)

    @property
    def totals_by_language(self) -> dict[str, LanguageTotal]:
        totals: dict[str, LanguageTotal] = {}
        for record in self.files:
            totals.setdefault(record.language, LanguageTotal(record.language)).add_file(record)
        return totals

    @property
    def total_files(self) -> int:
        return len(self.files)

    @property
    def total_ignored(self) -> int:
        return len(self.ignored_files)

    @property
    def total_blank(self) -> int:
        return sum(item.blank for item in self.files)

    @property
    def total_comment(self) -> int:
        return sum(item.comment for item in self.files)

    @property
    def total_code(self) -> int:
        return sum(item.code for item in self.files)

    @property
    def total_physical(self) -> int:
        return self.total_blank + self.total_comment + self.total_code

    def sorted_totals(self) -> list[LanguageTotal]:
        items = list(self.totals_by_language.values())
        return sorted(items, key=lambda item: (-item.code, item.language.lower()))

    def to_dict(self, by_file: bool = False) -> dict[str, Any]:
        data = {
            "root": self.root,
            "elapsed_seconds": self.elapsed_seconds,
            "total_files": self.total_files,
            "total_ignored": self.total_ignored,
            "total_blank": self.total_blank,
            "total_comment": self.total_comment,
            "total_code": self.total_code,
            "total_physical": self.total_physical,
            "languages": [item.to_dict() for item in self.sorted_totals()],
        }
        if by_file:
            data["files"] = [item.to_dict() for item in sorted(self.files, key=lambda row: row.path)]
        return data


@dataclass
class DiffRecord:
    language: str
    old_code: int = 0
    new_code: int = 0
    old_comment: int = 0
    new_comment: int = 0
    old_blank: int = 0
    new_blank: int = 0

    @property
    def delta_code(self) -> int:
        return self.new_code - self.old_code

    @property
    def delta_comment(self) -> int:
        return self.new_comment - self.old_comment

    @property
    def delta_blank(self) -> int:
        return self.new_blank - self.old_blank

    def to_dict(self) -> dict[str, int | str]:
        return {
            "language": self.language,
            "old_code": self.old_code,
            "new_code": self.new_code,
            "delta_code": self.delta_code,
            "old_comment": self.old_comment,
            "new_comment": self.new_comment,
            "delta_comment": self.delta_comment,
            "old_blank": self.old_blank,
            "new_blank": self.new_blank,
            "delta_blank": self.delta_blank,
        }
