from lxml import html
from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html, features="lxml")
    film_list = soup.find('td', {'class': 'region'})