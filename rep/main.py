# Многопоточный парсер с внесением данных в базу данных и отправкой данных в телеграм
# Вся логика проекта описана здесь

import threading
import time

from req import get_html
from parser import parse
from date import get_date

date = get_date()
url = f"https://www.mrsk-1.ru/ajax/disconn_list.php?region=67&district=55DE65CD-3A62-4304-BD72-75CB153B8F33&start={date[0][0]}.{date[0][1]}.{date[0][2]}&end={date[1][0]}.{date[1][1]}.{date[1][2]}"


def main():
    while True:
        html = get_html(url)  # GET запрос для получения данных об отключениях
        print(parse(html))
        time.sleep(86400)  # Ждём сутки, чтобы послать новый запрос


if __name__ == "__main__":
    main()
