import requests
import xml.etree.ElementTree as ET
import zipfile
import os

class CWEAPI:
    CWE_URL = "https://cwe.mitre.org/data/xml/cwec_v4.10.xml.zip"
    CWE_ZIP_PATH = "cwe_data.zip"
    CWE_XML_PATH = "cwe_data.xml"

    @staticmethod
    def fetch_cwe_data():
        try:
            print("Fetching CWE data...")
            response = requests.get(CWEAPI.CWE_URL)
            if response.status_code == 200:
                with open(CWEAPI.CWE_ZIP_PATH, "wb") as file:
                    file.write(response.content)
                print("CWE data downloaded successfully!")

                # Extract XML file from the ZIP archive
                with zipfile.ZipFile(CWEAPI.CWE_ZIP_PATH, "r") as zip_ref:
                    zip_ref.extractall()
                print("CWE data extracted successfully!")
            else:
                print(f"Failed to fetch CWE data. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching CWE data: {e}")

    @staticmethod
    def parse_cwe_data():
        try:
            if not os.path.exists(CWEAPI.CWE_XML_PATH):
                print("CWE XML file not found. Please fetch the data first.")
                return {}

            tree = ET.parse(CWEAPI.CWE_XML_PATH)
            root = tree.getroot()
            cwe_mapping = {}
            for weakness in root.findall(".//Weakness"):
                cwe_id = weakness.get("ID")
                name = weakness.get("Name")
                description = weakness.find("Description").text if weakness.find("Description") else "N/A"
                cwe_mapping[cwe_id] = {"name": name, "description": description}
            return cwe_mapping
        except Exception as e:
            print(f"Error parsing CWE data: {e}")
            return {}
