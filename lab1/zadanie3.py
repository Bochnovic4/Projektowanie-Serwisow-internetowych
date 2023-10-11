import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_station_data(station_url):
    response = requests.get(station_url)
    data = response.json()
    sensors_id = [sensor["id"]]


if __name__ == '__main__':
    station_id = '14'
    url = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
    