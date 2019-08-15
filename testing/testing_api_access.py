import requests
import json

BASE_URL = 'http://localhost:8000/'
API_ENDPOINT = 'api/updates/'

def get_data():
    data = requests.get(url=(BASE_URL + API_ENDPOINT + str(5) + '/'))
    print(data.json())
    # data = data.json()
    # print(data)
    # for obj in data:
    #     print(obj)
    #
    # for obj in data:
    #     print(obj['id'])

def post_data():
    new_data = {
        'content': ''
    }
    r = requests.delete(url=(BASE_URL+API_ENDPOINT + str(5) + '/'))
    # r = requests.post(url=(BASE_URL + API_ENDPOINT), data=new_data)
    print(r)
    print(r.status_code)
    print(r.json())

get_data()
post_data()
print('----------------')
get_data()