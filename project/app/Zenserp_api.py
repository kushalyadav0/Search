import os
from urllib import response
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ZENSCRAPE_API_KEY')

def Perform_search(query, search_type='web'):
    url = "https://app.zenserp.com/api/v2/search" # Zenserp's API Endpoint
    params = {
        'q':query,
        'api_key': API_KEY,
        'tbm': search_type,
    }

    response = requests.get(url, params=params)
    return response.json()