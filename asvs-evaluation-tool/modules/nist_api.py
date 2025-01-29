import requests

class NISTAPI:
    NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    API_KEY = "3afe4dda-4d13-4751-8b98-e170b49ca4e0" 

    @staticmethod
    def fetch_nist_data(keyword=None, results_per_page=10):
        try:
            params = {
                "resultsPerPage": results_per_page,
                "keyword": keyword,
                "apiKey": NISTAPI.API_KEY
            }
            response = requests.get(NISTAPI.NVD_URL, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch NIST data. Status code: {response.status_code}")
                return {}
        except Exception as e:
            print(f"Error fetching NIST data: {e}")
            return {}