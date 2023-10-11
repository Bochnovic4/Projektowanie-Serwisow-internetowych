import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def get_data(url: str):
    page = requests.get(url)
    s = BeautifulSoup(page.content, 'html.parser')
    ul_element = s.find('ul', class_='today-hourly-weather')
    li_elements = ul_element.find_all('li')

    temperature_data = []

    for li in li_elements:
        temp_span = li.find('span', class_='today-hourly-weather__temp')

        temperature = temp_span.get_text(strip=True)

        temperature_data.append(temperature)


    return temperature_data


def generate_plot(data):
    fig, ax = plt.subplots()
    data = [int(val) for val in data]
    time_of_day = ['Noc', 'Ranek', 'Dzień', 'Wieczór']
    ax.plot(time_of_day, data, marker='o', linestyle='-')
    ax.set_ylabel('temperatura')
    ax.set_title(f'temperatura w {city_name}')

    plt.show()

def process_string(input_str):
    result = ""
    is_negative = False

    for char in input_str:
        if char == '-':
            is_negative = True
        elif char.isdigit():
            result += char
        elif result and not char.isdigit():
            break

    if result:
        if is_negative:
            result = '-' + result

    return result

if __name__ == '__main__':
    url = 'https://www.meteoprog.pl/pl/weather/'
    city_name = 'Warszawa'
    url += city_name
    temperature = get_data(url)
    clean_data = []
    print(temperature)
    for item in temperature:
        clean_data.append(process_string(item))
    print(clean_data)
    generate_plot(clean_data)

