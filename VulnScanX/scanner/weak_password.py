# scanner/weak_password.py
import requests

class WeakPasswordScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for weak passwords...")
        # Example: Brute-force login (not recommended for real use)
        passwords = ["admin", "password", "123456"]
        for password in passwords:
            response = requests.post(self.target_url, data={"username": "admin", "password": password})
            if "login successful" in response.text.lower():
                print(f"Weak password found: {password}")