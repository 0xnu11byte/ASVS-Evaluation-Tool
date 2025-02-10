# ASVS-Evaluation-Tool
This project provides a scalable solution for implementing and evaluating the OWASP ASVS framework.

### Directory Structure
```
asvs-evaluation-tool/
├── main.py                # Entry point for the application
├── config/
│   ├── requirements.json  # JSON file containing ASVS requirements
│   └── cwe_nist_mappings.json # JSON file containing CWE/NIST mappings
├── modules/
│   ├── evaluator.py       # Core logic for evaluating requirements
│   ├── loader.py          # Module to load requirements from JSON
│   ├── reporter.py        # Module to generate reports
│   └── cwe_nist_mapper.py # Module to map CWE/NIST mappings
├── tests/
│    └── test_data.json    # Sample test cases for validation
└── reports/
    └── report.json        # Generated report
