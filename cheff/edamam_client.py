# edamam_client.py
import os
import requests
# Load environment variables
EDAMAM_APP_ID="8a2182d7"
EDAMAM_APP_KEY="38068d46f9afb422b2b3bc532841262d"

class EdamamClient:
    BASE_URL = "https://api.edamam.com"

    def __init__(self):
        self.app_id = EDAMAM_APP_ID
        self.app_key = EDAMAM_APP_KEY

    def analyze_recipe(self, title, ingredients):
        url = f"{self.BASE_URL}/api/nutrition-details"
        headers = {"Content-Type": "application/json"}
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key
        }
        data = {
            "title": title,
            "ingr": ingredients
        }

        response = requests.post(url, json=data, headers=headers, params=params)
        response.raise_for_status()  # Ensure successful response
        return response.json()
