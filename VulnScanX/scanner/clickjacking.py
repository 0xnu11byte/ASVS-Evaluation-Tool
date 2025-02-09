# scanner/clickjacking.py
import requests

class ClickjackingScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for clickjacking vulnerabilities...")
        response = requests.get(self.target_url)
        if "X-Frame-Options" not in response.headers:
            print("Potential clickjacking vulnerability: Missing X-Frame-Options header.")