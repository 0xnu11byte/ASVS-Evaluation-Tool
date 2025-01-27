import json

def load_requirements(file_path):
    # Loads ASVS requirements from a JSON file.
    with open(file_path, "r") as f:
        return json.load(f)