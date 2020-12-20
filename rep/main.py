# Многопоточный парсер с внесением данных в базу данных и отправкой данных в телеграм
import threading
import datetime
import time

from req import get_html
from parser import parse

start = str(datetime.datetime.now().month)

day = datetime.datetime.now().day
year_s = datetime.datetime.now().year
year_e = year_s

if start != "12":
    end = str(int(start)+1)
else:
    end = "01"
    year_e = str(int(year_s)+1)


print(f"https://www.mrsk-1.ru/ajax/disconn_list.php?region=67&district=55DE65CD-3A62-4304-BD72-75CB153B8F33&start={day}.{start}.{year_s}&end={day}.{end}.{year_e}")
url = f"https://www.mrsk-1.ru/ajax/disconn_list.php?region=67&district=55DE65CD-3A62-4304-BD72-75CB153B8F33&start={day}.{start}.{year_s}&end={day}.{end}.{year_e}"


def main():
    while True:
        html = get_html(url)  # GET запрос для получения данных об отключениях
        print(html)
        time.sleep(86400)


if __name__ == "__main__":
    main()
