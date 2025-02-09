# scanner/subdomain_enumeration.py
import requests

class SubdomainEnumerator:
    def __init__(self, target_domain):
        self.target_domain = target_domain

    def enumerate(self):
        print(f"Enumerating subdomains for {self.target_domain}...")
        subdomains = ["www", "mail", "ftp", "test"]
        for subdomain in subdomains:
            url = f"http://{subdomain}.{self.target_domain}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Found subdomain: {url}")
            except requests.RequestException:
                pass