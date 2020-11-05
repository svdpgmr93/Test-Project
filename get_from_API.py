import requests
URL_LST = [
    'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode=USD',
    'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode=EUR',
    'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode=RUB'
            ]


def get_data(url):
    data = requests.get(url).json()

    return data


for elem in URL_LST:
    print(get_data(elem)[0]['rate'])
