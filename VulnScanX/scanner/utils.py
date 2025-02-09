# scanner/utils.py
import requests

def is_url_accessible(url):
    """
    Check if a URL is accessible.
    """
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def calculate_security_score(issues_found):
    """
    Calculate a security score based on the number of issues found.
    The score is out of 100, with 100 being the most secure.
    """
    total_issues = sum(issues_found.values())
    
    # Define a scoring logic (customize as needed)
    if total_issues == 0:
        return 100  # No issues found, perfect score
    elif total_issues <= 5:
        return 80   # Few issues, good score
    elif total_issues <= 10:
        return 60   # Moderate issues, average score
    elif total_issues <= 20:
        return 40   # Many issues, poor score
    else:
        return 20   # Critical issues, very poor score