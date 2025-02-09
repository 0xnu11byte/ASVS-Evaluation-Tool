# scanner/security_headers.py
import requests

class SecurityHeadersScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for missing security headers...")
        response = requests.get(self.target_url)
        headers = response.headers

        required_headers = ["Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"]
        for header in required_headers:
            if header not in headers:
                print(f"Missing security header: {header}")