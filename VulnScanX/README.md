# VulnScanX

VulnScanX is a comprehensive vulnerability scanning tool designed to identify security issues in web applications. It provides a modular and extensible framework for performing various types of security tests, including SQL injection, XSS, directory traversal, and more.

---

## Features

- **Crawling**: Discover URLs on the target website.
- **SQL Injection Testing**: Test for SQL injection vulnerabilities.
- **Cross-Site Scripting (XSS) Testing**: Test for XSS vulnerabilities.
- **Security Headers Check**: Verify the presence of essential security headers.
- **Weak Password Testing**: Test for weak or common passwords.
- **CSRF Testing**: Test for Cross-Site Request Forgery (CSRF) vulnerabilities.
- **Directory Traversal Testing**: Test for directory traversal vulnerabilities.
- **File Inclusion Testing**: Test for local and remote file inclusion vulnerabilities.
- **Clickjacking Testing**: Test for clickjacking vulnerabilities.
- **SSL/TLS Testing**: Check for SSL/TLS misconfigurations.
- **Open Redirect Testing**: Test for open redirect vulnerabilities.
- **Command Injection Testing**: Test for command injection vulnerabilities.
- **Server-Side Request Forgery (SSRF) Testing**: Test for SSRF vulnerabilities.
- **API Security Testing**: Test for API-related vulnerabilities.
- **Brute Force Testing**: Test for weak authentication mechanisms.
- **Session Management Testing**: Test for session-related vulnerabilities.
- **CORS Testing**: Test for Cross-Origin Resource Sharing (CORS) misconfigurations.
- **Subdomain Enumeration**: Discover subdomains of the target domain.
- **Port Scanning**: Identify open ports on the target host.
- **Dependency Scanning**: Check for outdated or vulnerable dependencies.
- **Report Generation**: Generate a detailed report of the scan results, including a security score.

---

## Usage
Run the tool with the target URL and optional arguments:

```bash
python main.py <url> [options]
```

## Available Arguments

| Argument           | Description                                      |
|-------------------|--------------------------------------------------|
| `<url>`           | Target website URL to scan (required).          |
| `-d, --depth`     | Crawling depth (default: 2).                    |
| `-o, --output`    | Output file to save the report.                 |
| `--no-crawl`      | Disable crawling (only scan the provided URL).   |
| `--no-sql`        | Disable SQL Injection testing.                   |
| `--no-xss`        | Disable XSS testing.                             |
| `--no-headers`    | Disable Security Headers testing.                |
| `--no-passwords`  | Disable Weak Password testing.                   |
| `--no-csrf`       | Disable CSRF testing.                            |
| `--no-traversal`  | Disable Directory Traversal testing.             |
| `--no-inclusion`  | Disable File Inclusion testing.                  |
| `--no-clickjacking` | Disable Clickjacking testing.                 |
| `--no-ssl`        | Disable SSL/TLS testing.                         |
| `--no-redirect`   | Disable Open Redirect testing.                   |
| `--no-command`    | Disable Command Injection testing.               |
| `--no-ssrf`       | Disable SSRF testing.                            |
| `--no-api`        | Disable API Security testing.                    |
| `--no-brute`      | Disable Brute Force testing.                     |
| `--no-session`    | Disable Session Management testing.              |
| `--no-cors`       | Disable CORS testing.                            |
| `--no-subdomains` | Disable Subdomain Enumeration testing.           |
| `--no-ports`      | Disable Port Scanning testing.                   |
| `--no-dependencies` | Disable Dependency Scanning testing.           |

## Example Usage

```bash
python main.py https://example.com -d 3 -o report.txt --no-sql --no-xss
```

This command scans `https://example.com` with a crawling depth of `3`, saves the report to `report.txt`, and disables SQL Injection and XSS testing.

