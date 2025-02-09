# scanner/cors.py
import requests

class CORSScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for CORS misconfigurations...")
        response = requests.get(self.target_url)
        if "Access-Control-Allow-Origin" in response.headers:
            print("Potential CORS misconfiguration: Access-Control-Allow-Origin header found.")