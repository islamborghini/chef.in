# edamam_client.py
import os
import requests
from decouple import config
# Load environment variables
EDAMAM_APP_ID=config('EDAMAM_APP_ID')
EDAMAM_APP_KEY=config('EDAMAM_APP_KEY')

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
