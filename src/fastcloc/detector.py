from __future__ import annotations

from pathlib import Path
from .languages import extension_index, filename_index, iter_language_specs
from .models import LanguageSpec, ScanConfig

_EXTENSION_INDEX: dict[str, LanguageSpec] | None = None
_FILENAME_INDEX: dict[str, LanguageSpec] | None = None


def _get_extension_index() -> dict[str, LanguageSpec]:
    global _EXTENSION_INDEX
    if _EXTENSION_INDEX is None:
        _EXTENSION_INDEX = extension_index()
    return _EXTENSION_INDEX


def _get_filename_index() -> dict[str, LanguageSpec]:
    global _FILENAME_INDEX
    if _FILENAME_INDEX is None:
        _FILENAME_INDEX = filename_index()
    return _FILENAME_INDEX


def detect_by_filename(path: Path) -> LanguageSpec | None:
    return _get_filename_index().get(path.name.lower())


def detect_by_extension(path: Path, config: ScanConfig | None = None) -> LanguageSpec | None:
    suffix = path.suffix.lower().lstrip(".")
    if config and suffix in config.extra_extensions:
        from .models import LanguageSpec
        return LanguageSpec(name=config.extra_extensions[suffix], extensions=(suffix,))
    return _get_extension_index().get(suffix)


def read_first_line(path: Path, encoding: str = "utf-8", errors: str = "replace") -> str:
    with path.open("rb") as handle:
        raw = handle.readline(256)
    return raw.decode(encoding, errors=errors)


def detect_by_shebang(first_line: str) -> LanguageSpec | None:
    if not first_line.startswith("#!"):
        return None
    for spec in iter_language_specs():
        if spec.matches_shebang(first_line):
            return spec
    return None


def detect_language(path: Path, config: ScanConfig | None = None, first_line: str | None = None) -> LanguageSpec | None:
    exact = detect_by_filename(path)
    if exact is not None:
        return exact
    by_ext = detect_by_extension(path, config)
    if by_ext is not None:
        return by_ext
    if first_line is None:
        try:
            first_line = read_first_line(path, (config.encoding if config else "utf-8"), (config.errors if config else "replace"))
        except OSError:
            first_line = ""
    return detect_by_shebang(first_line)


def language_name_for_path(path: Path, config: ScanConfig | None = None, first_line: str | None = None) -> str:
    spec = detect_language(path, config=config, first_line=first_line)
    if spec is None:
        return "Text"
    return spec.name
