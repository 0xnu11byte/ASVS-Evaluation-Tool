import json
from modules.loader import load_requirements
from modules.evaluator import Evaluator
from modules.reporter import generate_report

# Load requirements
requirements_file = "config/requirements.json"
requirements = load_requirements(requirements_file)

# Initialize evaluator
evaluator = Evaluator(requirements)

# Load CWE data
evaluator.load_cwe_data()

# Fetch NIST data
evaluator.fetch_nist_data(keyword="authentication")

# Load test data
test_data_file = "tests/test_data.json"
with open(test_data_file, "r") as f:
    test_data = json.load(f)

# Evaluate categories
overall_results = {}
for category, data in test_data.items():
    print(f"Evaluating category: {category}...\n")
    results = evaluator.evaluate(category, data)
    overall_results[category] = results
    print(json.dumps(results, indent=4))

# Generate a report
generate_report(overall_results)
