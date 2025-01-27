import json

def generate_report(results, output_file="report.json"):
    # Generates a report in JSON format.
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
        print(f"Report generated: {output_file}")