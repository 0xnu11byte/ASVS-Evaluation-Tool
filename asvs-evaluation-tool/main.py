import json
from modules.loader import load_requirements
from modules.evaluator import Evaluator
from modules.reporter import generate_report

# Load requirements and test data
requirements_file = "config/requirements.json"
test_data_file = "tests/test_data.json"
requirements = load_requirements(requirements_file)

with open(test_data_file, "r") as f:
    test_data = json.load(f)

# Initialize evaluator and evaluate each category
evaluator = Evaluator(requirements)
overall_results = {}

for category, data in test_data.items():
    print(f"Evaluating category: {category}...\n")
    results = evaluator.evaluate(category, data)
    overall_results[category] = results
    print(json.dumps(results, indent=4))

# Generate a report
generate_report(overall_results)