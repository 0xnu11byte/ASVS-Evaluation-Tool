import argparse
from scanner.crawler import Crawler
from scanner.sql_injection import SQLInjectionScanner
from scanner.xss import XSSScanner
from scanner.security_headers import SecurityHeadersScanner
from scanner.weak_password import WeakPasswordScanner
from scanner.csrf import CSRFScanner
from scanner.directory_traversal import DirectoryTraversalScanner
from scanner.file_inclusion import FileInclusionScanner
from scanner.clickjacking import ClickjackingScanner
from scanner.ssl_tls import SSLTLSScanner
from scanner.open_redirect import OpenRedirectScanner
from scanner.command_injection import CommandInjectionScanner
from scanner.ssrf import SSRFScanner
from scanner.api_security import APISecurityScanner
from scanner.brute_force import BruteForceScanner
from scanner.session_management import SessionManagementScanner
from scanner.cors import CORSScanner
from scanner.subdomain_enumeration import SubdomainEnumerator
from scanner.port_scanning import PortScanner
from scanner.dependency_scanning import DependencyScanner
from scanner.report_generator import ReportGenerator
from scanner.utils import calculate_security_score


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="VulnScanX - A Comprehensive Vulnerability Scanner")
    parser.add_argument("url", help="Target website URL to scan")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Crawling depth (default: 2)")
    parser.add_argument("-o", "--output", help="Output file to save the report")
    parser.add_argument("--no-crawl", action="store_true", help="Disable crawling (only scan the provided URL)")
    parser.add_argument("--no-sql", action="store_true", help="Disable SQL Injection testing")
    parser.add_argument("--no-xss", action="store_true", help="Disable XSS testing")
    parser.add_argument("--no-headers", action="store_true", help="Disable Security Headers testing")
    parser.add_argument("--no-passwords", action="store_true", help="Disable Weak Password testing")
    parser.add_argument("--no-csrf", action="store_true", help="Disable CSRF testing")
    parser.add_argument("--no-traversal", action="store_true", help="Disable Directory Traversal testing")
    parser.add_argument("--no-inclusion", action="store_true", help="Disable File Inclusion testing")
    parser.add_argument("--no-clickjacking", action="store_true", help="Disable Clickjacking testing")
    parser.add_argument("--no-ssl", action="store_true", help="Disable SSL/TLS testing")
    parser.add_argument("--no-redirect", action="store_true", help="Disable Open Redirect testing")
    parser.add_argument("--no-command", action="store_true", help="Disable Command Injection testing")
    parser.add_argument("--no-ssrf", action="store_true", help="Disable SSRF testing")
    parser.add_argument("--no-api", action="store_true", help="Disable API Security testing")
    parser.add_argument("--no-brute", action="store_true", help="Disable Brute Force testing")
    parser.add_argument("--no-session", action="store_true", help="Disable Session Management testing")
    parser.add_argument("--no-cors", action="store_true", help="Disable CORS testing")
    parser.add_argument("--no-subdomains", action="store_true", help="Disable Subdomain Enumeration testing")
    parser.add_argument("--no-ports", action="store_true", help="Disable Port Scanning testing")
    parser.add_argument("--no-dependencies", action="store_true", help="Disable Dependency Scanning testing")
    args = parser.parse_args()

    # Initialize variables
    target_website = args.url
    issues_found = {}

    # Crawl the website (if enabled)
    if not args.no_crawl:
        print("[*] Crawling the website...")
        crawler = Crawler(target_website, max_depth=args.depth)
        crawler.crawl(target_website)
        urls_to_scan = crawler.get_visited_urls()
    else:
        urls_to_scan = [target_website]

    # Perform vulnerability scans
    for url in urls_to_scan:
        print(f"\n[*] Scanning: {url}")

        # SQL Injection Testing
        if not args.no_sql:
            print("[*] Testing for SQL Injection...")
            sql_tester = SQLInjectionScanner(url)
            sql_issues = sql_tester.scan()
            if sql_issues:
                issues_found["SQL Injection"] = issues_found.get("SQL Injection", 0) + len(sql_issues)

        # XSS Testing
        if not args.no_xss:
            print("[*] Testing for XSS...")
            xss_tester = XSSScanner(url)
            xss_issues = xss_tester.scan()
            if xss_issues:
                issues_found["XSS"] = issues_found.get("XSS", 0) + len(xss_issues)

        # Security Headers Testing
        if not args.no_headers:
            print("[*] Testing Security Headers...")
            headers_tester = SecurityHeadersScanner(url)
            missing_headers = headers_tester.scan()
            if missing_headers:
                issues_found["Missing Headers"] = issues_found.get("Missing Headers", 0) + len(missing_headers)

        # Weak Password Testing
        if not args.no_passwords:
            print("[*] Testing for Weak Passwords...")
            password_tester = WeakPasswordScanner(url)
            weak_passwords = password_tester.scan()
            if weak_passwords:
                issues_found["Weak Password"] = issues_found.get("Weak Password", 0) + len(weak_passwords)

        # CSRF Testing
        if not args.no_csrf:
            print("[*] Testing for CSRF...")
            csrf_tester = CSRFScanner(url)
            csrf_issues = csrf_tester.scan()
            if csrf_issues:
                issues_found["CSRF"] = issues_found.get("CSRF", 0) + len(csrf_issues)

        # Directory Traversal Testing
        if not args.no_traversal:
            print("[*] Testing for Directory Traversal...")
            dir_traversal_tester = DirectoryTraversalScanner(url)
            dir_traversal_issues = dir_traversal_tester.scan()
            if dir_traversal_issues:
                issues_found["Directory Traversal"] = issues_found.get("Directory Traversal", 0) + len(dir_traversal_issues)

        # File Inclusion Testing
        if not args.no_inclusion:
            print("[*] Testing for File Inclusion...")
            file_inclusion_tester = FileInclusionScanner(url)
            file_inclusion_issues = file_inclusion_tester.scan()
            if file_inclusion_issues:
                issues_found["File Inclusion"] = issues_found.get("File Inclusion", 0) + len(file_inclusion_issues)

        # Clickjacking Testing
        if not args.no_clickjacking:
            print("[*] Testing for Clickjacking...")
            clickjacking_tester = ClickjackingScanner(url)
            clickjacking_issue = clickjacking_tester.scan()
            if clickjacking_issue:
                issues_found["Clickjacking"] = issues_found.get("Clickjacking", 0) + 1

        # SSL/TLS Testing
        if not args.no_ssl:
            print("[*] Testing SSL/TLS Configuration...")
            ssl_tester = SSLTLSScanner(url)
            ssl_issue = ssl_tester.scan()
            if ssl_issue:
                issues_found["SSL/TLS Misconfiguration"] = issues_found.get("SSL/TLS Misconfiguration", 0) + 1

        # Open Redirect Testing
        if not args.no_redirect:
            print("[*] Testing for Open Redirect...")
            open_redirect_tester = OpenRedirectScanner(url)
            open_redirect_issues = open_redirect_tester.scan()
            if open_redirect_issues:
                issues_found["Open Redirect"] = issues_found.get("Open Redirect", 0) + len(open_redirect_issues)

        # Command Injection Testing
        if not args.no_command:
            print("[*] Testing for Command Injection...")
            command_tester = CommandInjectionScanner(url)
            command_issues = command_tester.scan()
            if command_issues:
                issues_found["Command Injection"] = issues_found.get("Command Injection", 0) + len(command_issues)

        # SSRF Testing
        if not args.no_ssrf:
            print("[*] Testing for SSRF...")
            ssrf_tester = SSRFScanner(url)
            ssrf_issues = ssrf_tester.scan()
            if ssrf_issues:
                issues_found["SSRF"] = issues_found.get("SSRF", 0) + len(ssrf_issues)

        # API Security Testing
        if not args.no_api:
            print("[*] Testing API Security...")
            api_tester = APISecurityScanner(url)
            api_issues = api_tester.scan()
            if api_issues:
                issues_found["API Security"] = issues_found.get("API Security", 0) + len(api_issues)

        # Brute Force Testing
        if not args.no_brute:
            print("[*] Testing for Brute Force...")
            brute_tester = BruteForceScanner(url)
            brute_issues = brute_tester.scan()
            if brute_issues:
                issues_found["Brute Force"] = issues_found.get("Brute Force", 0) + len(brute_issues)

        # Session Management Testing
        if not args.no_session:
            print("[*] Testing Session Management...")
            session_tester = SessionManagementScanner(url)
            session_issues = session_tester.scan()
            if session_issues:
                issues_found["Session Management"] = issues_found.get("Session Management", 0) + len(session_issues)

        # CORS Testing
        if not args.no_cors:
            print("[*] Testing CORS...")
            cors_tester = CORSScanner(url)
            cors_issues = cors_tester.scan()
            if cors_issues:
                issues_found["CORS"] = issues_found.get("CORS", 0) + len(cors_issues)

        # Subdomain Enumeration
        if not args.no_subdomains:
            print("[*] Enumerating Subdomains...")
            subdomain_tester = SubdomainEnumerator(url)
            subdomains = subdomain_tester.enumerate()
            if subdomains:
                issues_found["Subdomains"] = issues_found.get("Subdomains", 0) + len(subdomains)

        # Port Scanning
        if not args.no_ports:
            print("[*] Scanning Ports...")
            port_tester = PortScanner(url)
            open_ports = port_tester.scan()
            if open_ports:
                issues_found["Open Ports"] = issues_found.get("Open Ports", 0) + len(open_ports)

        # Dependency Scanning
        if not args.no_dependencies:
            print("[*] Scanning Dependencies...")
            dependency_tester = DependencyScanner(url)
            outdated_deps = dependency_tester.scan()
            if outdated_deps:
                issues_found["Outdated Dependencies"] = issues_found.get("Outdated Dependencies", 0) + len(outdated_deps)

    # Calculate Security Score
    security_score = calculate_security_score(issues_found)

    # Generate Report
    print("\n[*] Generating report...")
    report_generator = ReportGenerator(issues_found, security_score)
    report_content = report_generator.generate_report()

    # Print report to console
    print("\n=== Scan Report ===")
    print(report_content)

    # Save report to file (if output file is provided)
    if args.output:
        with open(args.output, "w") as f:
            f.write(report_content)
        print(f"[*] Report saved to {args.output}")


if __name__ == "__main__":
    main()