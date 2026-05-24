"""FastCLOC-Py public package API."""
from .api import analyze_path, analyze_text, compare_paths
from .models import FileRecord, LanguageSpec, LanguageTotal, ScanConfig, ScanSummary

__all__ = [
    "analyze_path",
    "analyze_text",
    "compare_paths",
    "FileRecord",
    "LanguageSpec",
    "LanguageTotal",
    "ScanConfig",
    "ScanSummary",
]

__version__ = "0.1.0"
