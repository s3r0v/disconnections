# Скрипт определяет сегодняшнее число и интервал
import datetime
import time

start_date = []
end_date = []


def get_date():
    start_date.append(str(datetime.datetime.now().day))
    start_date.append(str(datetime.datetime.now().month))
    start_date.append(str(datetime.datetime.now().year))

    if start_date[1] == "12":
        end_date.append(str(int(start_date[0])))
        end_date.append("01")
        end_date.append(str(int(start_date[2]) + 1))
    else:
        end_date.append(str(int(start_date[0])))
        end_date.append(str(int(start_date[1]) + 1))
        end_date.append(str(int(start_date[2])))

    date = [start_date, end_date]
    return date
