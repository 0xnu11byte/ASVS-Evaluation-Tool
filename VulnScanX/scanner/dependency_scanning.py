# scanner/dependency_scanning.py
import requests

class DependencyScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for outdated dependencies...")
        response = requests.get(self.target_url)
        if "jquery" in response.text:
            print("Potential outdated dependency: jQuery found.")