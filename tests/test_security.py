import tempfile
import unittest
from pathlib import Path
from fastcloc.security import is_binary_bytes, inspect_file
from fastcloc.models import ScanConfig


class SecurityTests(unittest.TestCase):
    def test_binary_detection(self):
        self.assertTrue(is_binary_bytes(b"abc\x00def"))
        self.assertFalse(is_binary_bytes(b"print('hello')\n"))

    def test_max_size_rejection(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "big.py"
            path.write_text("x = 1\n", encoding="utf-8")
            ok, reason, size = inspect_file(path, ScanConfig(max_file_bytes=1))
            self.assertFalse(ok)
            self.assertIn("file too large", reason)
            self.assertGreater(size, 1)


if __name__ == "__main__":
    unittest.main()
