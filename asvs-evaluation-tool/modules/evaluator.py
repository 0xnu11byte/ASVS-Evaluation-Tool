from .cwe_api import CWEAPI
from .nist_api import NISTAPI

class Evaluator:
    def __init__(self, requirements):
        self.requirements = requirements
        self.cwe_mapping = {}
        self.nist_data = {}

    def load_cwe_data(self):
        CWEAPI.fetch_cwe_data()
        self.cwe_mapping = CWEAPI.parse_cwe_data()

    def fetch_nist_data(self, keyword):
        self.nist_data = NISTAPI.fetch_nist_data(keyword=keyword)

    def evaluate(self, category, data):
        results = {}
        if category not in self.requirements:
            return {"error": f"Category '{category}' not found."}

        for req, details in self.requirements[category].items():
            check = self._get_check(req)
            if check:
                results[req] = {
                    "requirement": details["requirement"],
                    "status": "Pass" if check(data.get(req, "")) else "Fail",
                    "cwe": self.get_cwe_for_requirement(req),
                    "nist": self.get_nist_for_requirement(req)
                }
            else:
                results[req] = {
                    "requirement": details["requirement"],
                    "status": "Error: No validation logic implemented."
                }
        return results

    def get_cwe_for_requirement(self, req):
        return self.cwe_mapping.get(req, {"name": "Unknown", "description": "No CWE mapping found"})

    def get_nist_for_requirement(self, req):
        return {"nist_controls": self.nist_data.get(req, "No NIST mapping found")}

    def _get_check(self, req):
        checks = {
            "password_length": lambda pwd: len(pwd) >= 12,
            "password_storage": lambda hashed: hashed.startswith("$2b$"),
            "multi_factor_authentication": lambda mfa: mfa == "enabled"
        }
        return checks.get(req)
