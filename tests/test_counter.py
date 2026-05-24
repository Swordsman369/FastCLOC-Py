import unittest
from pathlib import Path
from fastcloc.api import analyze_text, analyze_path
from fastcloc.models import ScanConfig


class CounterTests(unittest.TestCase):
    def test_python_text_count(self):
        text = "\n".join([
            "# module comment",
            "x = 1  # inline comment",
            "",
            "\"\"\"block",
            "comment\"\"\"",
            "print(x)",
        ])
        result = analyze_text(text, "Python")
        self.assertEqual(result["blank"], 1)
        self.assertEqual(result["comment"], 3)
        self.assertEqual(result["code"], 2)

    def test_c_block_comment_count(self):
        text = "\n".join([
            "int x = 0;",
            "/* comment one",
            "comment two */",
            "int y = 1; /* inline block */",
        ])
        result = analyze_text(text, "C")
        self.assertEqual(result["comment"], 2)
        self.assertEqual(result["code"], 2)

    def test_path_count_fixture(self):
        root = Path(__file__).parent / "fixtures"
        summary = analyze_path(root, ScanConfig(include_hidden=True))
        self.assertGreaterEqual(summary.total_files, 2)
        self.assertGreater(summary.total_code, 0)
        languages = {row.language for row in summary.sorted_totals()}
        self.assertIn("Python", languages)
        self.assertIn("JavaScript", languages)


if __name__ == "__main__":
    unittest.main()
