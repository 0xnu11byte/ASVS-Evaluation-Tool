# scanner/session_management.py
import requests

class SessionManagementScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for session management issues...")
        response = requests.get(self.target_url)
        if "sessionid" in response.cookies:
            print("Potential session management issue: Session ID exposed.")