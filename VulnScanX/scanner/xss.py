# scanner/xss.py
import requests

class XSSScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for XSS vulnerabilities...")
        payload = "<script>alert('XSS')</script>"
        response = requests.get(self.target_url + payload)
        if payload in response.text:
            print(f"Potential XSS vulnerability found with payload: {payload}")