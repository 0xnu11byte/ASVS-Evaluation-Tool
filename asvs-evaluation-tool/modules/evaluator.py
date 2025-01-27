class Evaluator:
    def __init__(self, requirements):
        self.requirements = requirements

    def evaluate(self, category, data):
        results = {}
        if category not in self.requirements:
            return {"error": f"Category '{category}' not found."}

        for req, details in self.requirements[category].items():
            check = self._get_check(req)
            if check:
                results[req] = {
                    "requirement": details["requirement"],
                    "status": "Pass" if check(data.get(req, "")) else "Fail"
                }
            else:
                results[req] = {
                    "requirement": details["requirement"],
                    "status": "Error: No validation logic implemented."
                }
        return results

    def _get_check(self, req):
        # Maps requirement keys to their validation functions.
        checks = {
            "password_length": lambda pwd: len(pwd) >= 12,
            "password_storage": lambda hashed: hashed.startswith("$2b$"),
            "multi_factor_authentication": lambda mfa: mfa == "enabled",
            "sql_injection": lambda query: "DROP" not in query.upper(),
            "xss_protection": lambda input_data: "<script>" not in input_data.lower(),
            "input_length_validation": lambda input_data: len(input_data) <= 255,
            "path_traversal_prevention": lambda input_data: ".." not in input_data,
            "session_timeout": lambda timeout: int(timeout.split()[0]) <= 15,
            "secure_cookie_flag": lambda flag: flag is True,
            "http_only_cookie_flag": lambda flag: flag is True,
            "csrf_token": lambda token: token == "valid_token",
            "tls_enforcement": lambda version: version >= "TLS 1.2",
            "encryption_key_rotation": lambda date: int(date.split("-")[0]) >= 2023,
            "strong_hashing_algorithms": lambda algo: algo in ["SHA-256", "SHA-512"],
            "role_based_access": lambda status: status == "enabled",
            "least_privilege": lambda status: status == "enforced",
            "account_lockout": lambda attempts: int(attempts.split()[0]) >= 5
        }
        return checks.get(req)