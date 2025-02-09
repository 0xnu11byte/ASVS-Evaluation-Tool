# scanner/ssrf.py
import requests

class SSRFScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for SSRF vulnerabilities...")
        payloads = ["?url=http://internal", "?url=file:///etc/passwd"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "internal" in response.text or "root:" in response.text:
                print(f"Potential SSRF vulnerability found with payload: {payload}")