import requests
from config import API_RIA_key
URL = 'https://developers.ria.com/auto/search?api_key='


def get_data(url, api, params=None):
    data = requests.get(url + api + params)
    return data.json()


print(get_data(URL, API_RIA_key, '&price_ot=1000&price_do=60000'))
