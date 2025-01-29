import json

def generate_report(results, output_file="outputs/report.json"):
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Report generated at {output_file}")