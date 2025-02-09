# tests/test_sql_injection.py
import unittest
from scanner.sql_injection import SQLInjectionScanner

class TestSQLInjectionScanner(unittest.TestCase):
    def test_scan(self):
        scanner = SQLInjectionScanner("http://example.com")
        scanner.scan()

if __name__ == "__main__":
    unittest.main()