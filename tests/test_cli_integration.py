import json
import subprocess
import sys
import unittest
from pathlib import Path


class CliIntegrationTests(unittest.TestCase):
    def test_cli_table_fixture(self):
        root = Path(__file__).parent / "fixtures"
        proc = subprocess.run(
            [sys.executable, "-m", "fastcloc.cli", str(root), "--format", "table"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertIn("SUM", proc.stdout)
        self.assertIn("Python", proc.stdout)

    def test_cli_json_fixture(self):
        root = Path(__file__).parent / "fixtures"
        proc = subprocess.run(
            [sys.executable, "-m", "fastcloc.cli", str(root), "--format", "json", "--by-file"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        data = json.loads(proc.stdout)
        self.assertEqual(data["total_files"], 2)
        self.assertGreater(data["total_code"], 0)


if __name__ == "__main__":
    unittest.main()
