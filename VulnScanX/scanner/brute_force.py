# scanner/brute_force.py
import requests

class BruteForceScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for brute-force vulnerabilities...")
        passwords = ["admin", "password", "123456"]
        for password in passwords:
            response = requests.post(self.target_url, data={"username": "admin", "password": password})
            if "login successful" in response.text.lower():
                print(f"Weak password found: {password}")