# Парсер с внесением данных в базу данных и отправкой данных в телеграм
# Вся логика проекта описана здесь

import time
import sqlite3

from req import get_html
from parser import parse
from date import get_date
from db import create_table, send_data_to_db
from tg import send_data_to_tg, check_disconnection



def main():
    sent_data_tg = [] # Данные об отключениях, которые были отправлены в телеграм
    sent_data_db = [] # Данные об отключениях, которые были отправлены в базу данных 
    create_table() # Создаём таблицу отключений в базе данных

    while True:
        date = get_date()
        url = f"https://www.mrsk-1.ru/ajax/disconn_list.php?region=67&district=55DE65CD-3A62-4304-BD72-75CB153B8F33&start={date[0][0]}.{date[0][1]}.{date[0][2]}&end={date[1][0]}.{date[1][1]}.{date[1][2]}"
        
        html = get_html(url)  # GET запрос для получения данных об отключениях
        results = parse(html)

        sent_data_tg = send_data_to_tg(results,sent_data_tg)
        sent_data_db = send_data_to_db(results,sent_data_db)

        

        time.sleep(10)


if __name__ == "__main__":
    main()
