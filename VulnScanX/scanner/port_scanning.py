# scanner/port_scanning.py
import socket
from urllib.parse import urlparse

class PortScanner:
    def __init__(self, target_url):
        """
        Initialize the PortScanner with a target URL.
        """
        parsed_url = urlparse(target_url)
        self.target_host = parsed_url.hostname  # Extract hostname from URL
        if not self.target_host:
            raise ValueError(f"Invalid URL: {target_url}")

    def scan(self):
        """
        Scan common ports on the target host.
        """
        print(f"Scanning ports for {self.target_host}...")
        open_ports = []
        ports = [21, 22, 80, 443, 8080]  # Common ports to scan

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((self.target_host, port))
                if result == 0:
                    print(f"Port {port} is open.")
                    open_ports.append(port)
            except socket.error as e:
                print(f"Error scanning port {port}: {e}")
            finally:
                sock.close()

        return open_ports