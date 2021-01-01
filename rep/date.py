# Скрипт определяет сегодняшнее число и интервал
import datetime
import time

start_date = []
end_date = []

tomorrow = []
three_days = []
week = []

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

def day_add():
    today = datetime.now()
    tomorrow = presentday + timedelta(1)
    tomorrow = tomorrow.strftime['%d','%m','%Y']
    
    three_days = presentday + timedelta(3)
    three_days = three_days.strftime['%d','%m','%Y']
    
    week = presentday + timedelta(7)
    week = week.strftime['%d','%m','%Y']
    return (tomorrow, three_days, week)


    