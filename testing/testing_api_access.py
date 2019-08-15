import requests
import json

BASE_URL = 'http://localhost:8000/'
API_ENDPOINT = 'api/updates/'

def get_data():
    data = requests.get(url=(BASE_URL + API_ENDPOINT))
    data = data.json()
    for obj in data:
        print(obj)

    for obj in data:
        print(obj['id'])

def post_data():
    new_data = {
        'user': 1,
        'content': 'New script content'
    }
    r = requests.post(url=(BASE_URL+API_ENDPOINT), data=new_data)
    print(r)
    print(r.headers)
    print(r.status_code)
    if r.status_code == 200:
        print(r.json())

post_data()