# tests/test_xss.py
import unittest
from scanner.xss import XSSScanner

class TestXSSScanner(unittest.TestCase):
    def test_scan(self):
        scanner = XSSScanner("http://example.com")
        scanner.scan()

if __name__ == "__main__":
    unittest.main()