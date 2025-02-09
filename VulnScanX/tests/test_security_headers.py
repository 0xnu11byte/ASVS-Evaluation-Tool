# tests/test_security_headers.py
import unittest
from scanner.security_headers import SecurityHeadersScanner

class TestSecurityHeadersScanner(unittest.TestCase):
    def test_scan(self):
        scanner = SecurityHeadersScanner("http://example.com")
        scanner.scan()

if __name__ == "__main__":
    unittest.main()