# edamam_client.py
import os
import requests
from decouple import config

# Load environment variables
EDAMAM_APP_ID = config('EDAMAM_APP_ID')
EDAMAM_APP_KEY = config('EDAMAM_APP_KEY')

class EdamamClient:
    BASE_URL = "https://api.edamam.com"

    def __init__(self):
        # Initialize the client with app ID and app key from environment variables
        self.app_id = EDAMAM_APP_ID
        self.app_key = EDAMAM_APP_KEY

    def analyze_recipe(self, title, ingredients):
        # Define the URL for the nutrition analysis API endpoint
        url = f"{self.BASE_URL}/api/nutrition-details"
        # Set the request headers
        headers = {"Content-Type": "application/json"}
        # Set the request parameters
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key
        }
        # Set the request body with the recipe title and ingredients
        data = {
            "title": title,
            "ingr": ingredients
        }

        # Make the POST request to the API endpoint
        response = requests.post(url, json=data, headers=headers, params=params)
        response.raise_for_status()  # Ensure successful response
        # Return the JSON response from the API
        return response.json()
