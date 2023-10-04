import requests
from bs4 import BeautifulSoup
import numpy
import matplotlib.pyplot as plt


def get_data(url: str):
    page = requests.get(url)
    s = BeautifulSoup(page.content, 'html.parser')
    data = s.find_all('div', class_='times-of-day')
    result = []
    for row in data:
        temperature = row.find('li', {'class': 'temperature'}).text.strip()
        result.append(temperature)
    return result


def generate_plot(data):
    pass


if __name__ == '__main__':
    url = 'https://www.meteoprog.pl/pl/weather/'
    nazwa_miasta = 'Olsztyn'
    url += nazwa_miasta
    temperature = get_data(url)
    clean_data = []
    for item in temperature:
        item.remove('C')
        item.remove('°')
        clean_data.append(item)
    print(temperature)
