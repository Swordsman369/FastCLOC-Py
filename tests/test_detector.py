import unittest
from pathlib import Path
from fastcloc.api import detect_path_language
from fastcloc.detector import detect_by_shebang


class DetectorTests(unittest.TestCase):
    def test_extension_detection(self):
        self.assertEqual(detect_path_language(Path("demo.py")), "Python")
        self.assertEqual(detect_path_language(Path("demo.rs")), "Rust")
        self.assertEqual(detect_path_language(Path("Dockerfile")), "Dockerfile")

    def test_shebang_detection(self):
        spec = detect_by_shebang("#!/usr/bin/env python3")
        self.assertIsNotNone(spec)
        self.assertEqual(spec.name, "Python")


if __name__ == "__main__":
    unittest.main()
