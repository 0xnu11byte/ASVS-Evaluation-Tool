# scanner/report_generator.py
import datetime

class ReportGenerator:
    def __init__(self, findings):
        self.findings = findings

    def generate(self):
        print("Generating report...")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("report.txt", "w") as f:
            f.write(f"Vulnerability Scan Report - {timestamp}\n")
            f.write("=" * 40 + "\n")
            for finding in self.findings:
                f.write(f"- {finding}\n")
        print("Report generated: report.txt")