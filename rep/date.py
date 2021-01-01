# Скрипт определяет сегодняшнее число и интервал
import time
import datetime

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



def day_add():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(1)
    if len(str(tomorrow.day)) == 1 and len(str(tomorrow.month)) == 1:
        tomorrow = (f'0{tomorrow.day}.0{tomorrow.month}.{tomorrow.year}')

    elif len(str(tomorrow.day)) == 1 and len(str(tomorrow.month)) == 2:
        tomorrow = (f'0{tomorrow.day}.{tomorrow.month}.{tomorrow.year}')

    elif len(str(tomorrow.day)) == 2 and len(str(tomorrow.month)) == 1:
        tomorrow = (f'{tomorrow.day}.0{tomorrow.month}.{tomorrow.year}')

    else:
        tomorrow = (f'{tomorrow.day}.{tomorrow.month}.{tomorrow.year}')



    three_days = today + datetime.timedelta(3)
    if len(str(three_days.day)) == 1 and len(str(three_days.month)) == 1:
        three_days = (f'0{three_days.day}.0{three_days.month}.{three_days.year}')

    elif len(str(three_days.day)) == 1 and len(str(three_days.month)) == 2:
        three_days = (f'0{three_days.day}.{three_days.month}.{three_days.year}')

    elif len(str(three_days.day)) == 2 and len(str(three_days.month)) == 1:
        three_days = (f'{three_days.day}.0{three_days.month}.{three_days.year}')

    else:
        three_days = (f'{three_days.day}.{three_days.month}.{three_days.year}')

    

    week = today + datetime.timedelta(7)
    if len(str(week.day)) == 1 and len(str(week.month)) == 1:
        week = (f'0{week.day}.0{week.month}.{week.year}')

    elif len(str(week.day)) == 1 and len(str(week.month)) == 2:
        week = (f'0{week.day}.{week.month}.{week.year}')

    elif len(str(week.day)) == 2 and len(str(week.month)) == 1:
        week = (f'{week.day}.0{week.month}.{week.year}')

    else:
        week = (f'{week.day}.{week.month}.{week.year}')

    return(tomorrow,three_days,week)



    


    