# scanner/sql_injection.py
import requests

class SQLInjectionScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for SQL Injection vulnerabilities...")
        # Example payloads
        payloads = ["' OR '1'='1", "' OR 'a'='a"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "error" in response.text.lower():
                print(f"Potential SQL Injection vulnerability found with payload: {payload}")