import requests
from bs4 import BeautifulSoup
import json
import time


outfile = open('out.txt', 'r')
URL = 'https://finance.liga.net/currency'
prices = []


'''Get the all html data from site'''


def get_data(url):
    data = requests.get(url)
    return data.text


'''Get the target divs with prices'''


def start(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='table-wrap')
    td = table.findAll('div')
    return td


'''Extract the prices from divs'''


def text(div):
    soup = BeautifulSoup(div, 'html.parser')
    price = soup.find('div')
    return price.text


'''Main function with time delay'''


def run():
    page = get_data(URL)
    data = start(page)
    for elem in data:
        prices.append(text(str(elem)))
    with open('out.txt', 'w') as fw:
        json.dump(prices, fw)
    time.sleep(86400)
    run()


run()
