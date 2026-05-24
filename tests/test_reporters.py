import json
import unittest
from pathlib import Path
from fastcloc.api import analyze_path
from fastcloc.reporters import render_csv, render_json, render_markdown, render_table


class ReporterTests(unittest.TestCase):
    def setUp(self):
        self.summary = analyze_path(Path(__file__).parent / "fixtures")

    def test_json_report(self):
        data = json.loads(render_json(self.summary, by_file=True))
        self.assertIn("languages", data)
        self.assertIn("files", data)

    def test_csv_report(self):
        csv_text = render_csv(self.summary)
        self.assertIn("language,files,blank,comment,code,total", csv_text)

    def test_markdown_report(self):
        md = render_markdown(self.summary)
        self.assertIn("| Language |", md)
        self.assertIn("**SUM**", md)

    def test_table_report(self):
        table = render_table(self.summary)
        self.assertIn("Language", table)
        self.assertIn("SUM", table)


if __name__ == "__main__":
    unittest.main()
