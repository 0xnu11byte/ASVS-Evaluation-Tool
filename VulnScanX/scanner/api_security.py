# scanner/api_security.py
import requests

class APISecurityScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for API security issues...")
        response = requests.get(self.target_url)
        if "api" in response.text:
            print("Potential API security issue: Sensitive data exposed.")