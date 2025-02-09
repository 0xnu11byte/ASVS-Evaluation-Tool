import requests
from bs4 import BeautifulSoup
import urllib.parse
import matplotlib.pyplot as plt
from tqdm import tqdm
from selenium import webdriver

# Security Score Variables
security_score = 100
issues_found = {}

# Vulnerability Payloads
SQLI_PAYLOADS = ["' OR '1'='1", "'; DROP TABLE users; --", "\" OR \"1\"=\"1"]
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "'\"><script>alert(1)</script>",
    "'><svg onload=alert(1)>",
    "<iframe src=javascript:alert(1)>",
]
COMMON_PASSWORDS = ["admin", "password123", "123456", "qwerty", "test"]

# Headers to check
SECURITY_HEADERS = ["Content-Security-Policy", "Strict-Transport-Security", "X-Frame-Options", "X-XSS-Protection"]

# Visited URLs
visited_urls = set()

# 🛠 Function to crawl a website
def crawl(url, depth=2):
    if depth == 0 or url in visited_urls:
        return
    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract Links & Forms
        for link in soup.find_all("a", href=True):
            new_url = urllib.parse.urljoin(url, link["href"])
            if new_url.startswith("http"):
                crawl(new_url, depth - 1)

        test_sql_injection(url)
        test_xss(url)
        test_security_headers(url, response.headers)
        test_weak_password(url)
    except requests.RequestException:
        pass

# 🛠 Function to test SQL Injection
def test_sql_injection(url):
    global security_score
    for payload in SQLI_PAYLOADS:
        vuln_url = f"{url}?id={urllib.parse.quote(payload)}"
        response = requests.get(vuln_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print(f"[🔥] SQL Injection Found: {vuln_url}")
            security_score -= 10
            issues_found["SQL Injection"] = issues_found.get("SQL Injection", 0) + 1

# 🛠 Function to test XSS using Requests (basic check)
def test_xss(url):
    global security_score
    response = requests.get(url)
    
    for payload in XSS_PAYLOADS:
        vuln_url = f"{url}?q={urllib.parse.quote(payload)}"
        response = requests.get(vuln_url)

        # Check if the payload is reflected in response
        if payload in response.text or "<script>" in response.text or "alert(" in response.text:
            print(f"[🔥] XSS Found: {vuln_url}")
            security_score -= 8
            return
    
    # Use Selenium for JavaScript execution testing
    test_xss_selenium(url)

# 🛠 Function to test XSS using Selenium (Advanced Check)
def test_xss_selenium(url):
    global security_score
    driver = webdriver.Firefox()  # Use `webdriver.Chrome()` if using ChromeDriver

    for payload in XSS_PAYLOADS:
        test_url = f"{url}?q={urllib.parse.quote(payload)}"
        driver.get(test_url)

        # Check if the payload is executed in the browser
        if payload in driver.page_source:
            print(f"[🔥] XSS Found (Executed in Browser): {test_url}")
            security_score -= 8
            driver.quit()
            return
    
    driver.quit()

# 🛠 Function to check security headers
def test_security_headers(url, headers):
    global security_score
    missing_headers = [h for h in SECURITY_HEADERS if h not in headers]
    if missing_headers:
        print(f"[⚠️] Missing Security Headers at {url}: {missing_headers}")
        security_score -= len(missing_headers) * 2
        issues_found["Missing Headers"] = len(missing_headers)

# 🛠 Function to test weak passwords (login brute-force)
def test_weak_password(url):
    global security_score
    for password in COMMON_PASSWORDS:
        response = requests.post(url, data={"username": "admin", "password": password})
        if "incorrect password" not in response.text.lower():
            print(f"[🔥] Weak Password Found: {password} at {url}")
            security_score -= 10
            issues_found["Weak Password"] = issues_found.get("Weak Password", 0) + 1
            break

# 📊 Function to visualize results
def generate_report():
    labels = list(issues_found.keys())
    values = list(issues_found.values())

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['red', 'blue', 'orange'])
    plt.xlabel("Vulnerability Type")
    plt.ylabel("Occurrences")
    plt.title(f"Website Security Score: {security_score}/100")
    plt.show()

# 🚀 Run the Security Scanner
target_website = input("Enter the target website URL: ")
crawl(target_website)

# 📝 Generate Final Report
print(f"\n✅ Final Security Score: {security_score}/100")
generate_report()
