# scanner/open_redirect.py
import requests

class OpenRedirectScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for open redirect vulnerabilities...")
        payloads = ["?redirect=http://evil.com", "?url=http://evil.com"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "evil.com" in response.url:
                print(f"Potential open redirect vulnerability found with payload: {payload}")