# В скрипте описана вся логика парсера
from lxml import html as h
from bs4 import BeautifulSoup

def parse(html):
    html = h.fromstring(html) # Преобразует строку в HTML
    div_node = html.xpath('//div') # div тег
    return(div_node)