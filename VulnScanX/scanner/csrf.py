# scanner/csrf.py
import requests

class CSRFScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for CSRF vulnerabilities...")
        response = requests.get(self.target_url)
        if "csrf_token" not in response.text:
            print("Potential CSRF vulnerability: No CSRF token found.")