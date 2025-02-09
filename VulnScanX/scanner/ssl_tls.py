# scanner/ssl_tls.py
import requests

class SSLTLSScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        print(f"Scanning {self.target_url} for SSL/TLS misconfigurations...")
        try:
            response = requests.get(self.target_url)
            if response.url.startswith("https://"):
                print("SSL/TLS is properly configured.")
            else:
                print("Potential SSL/TLS misconfiguration: Not using HTTPS.")
        except requests.exceptions.SSLError:
            print("Potential SSL/TLS misconfiguration: Invalid certificate.")