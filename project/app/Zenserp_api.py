import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ZENSERP_API_KEY')

def Perform_search(query, search_type='web'):
    url = "https://app.zenserp.com/api/v2/search" # Zenserp's API Endpoint
    params = {
        'q':query,
        'apikey': API_KEY,
        'tbm': search_type,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()        
        data = response.json()
        

            # Optional: only extract relevant part
        return {
            "organic": data.get("organic", []),  # list of result dicts
            }
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching results: {e}")
        return {"organic": []}