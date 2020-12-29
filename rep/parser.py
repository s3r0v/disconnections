# В скрипте описана вся логика парсера
from lxml import html as h
from bs4 import BeautifulSoup
import asyncio

def parse(html):
    results = []
    html = BeautifulSoup(html,features="lxml")
    disconnections = html.find_all('tr')

    for disconnection in disconnections:
        location = disconnection.find('td', {'class': 'location'}).text

        if location != "г Сычевка" and disconnection not in results:
            results.append({
                    'region': disconnection.find('td', {'class': 'location'}).text,
                    'district': disconnection.find('td', {'class': 'district'}).text,
                    'location': location,
                    'object': disconnection.find('td', {'class': 'object'}).text,
                    'disconn-start-date': disconnection.find('td', {'class': 'disconn-start-date'}).text,
                    'disconn-start-time': disconnection.find('td', {'class': 'disconn-start-time'}).text,
                    'disconn-end-date': disconnection.find('td', {'class': 'disconn-end-date'}).text,
                    'disconn-end-time': disconnection.find('td', {'class': 'disconn-end-time'}).text,
                    'branch': disconnection.find('td', {'class': 'branch'}).text,
                    'res_title': disconnection.find('td', {'class': 'res_title'}).text,
                })
        else:
            continue
    return(results)