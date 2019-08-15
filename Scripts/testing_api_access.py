import requests
import json

BASE_URL = 'http://localhost:8000/'
API_ENDPOINT = 'api/updates/'

def get_data():
    data = requests.get(url=(BASE_URL + API_ENDPOINT))
    print(data)

get_data()