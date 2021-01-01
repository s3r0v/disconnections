import telebot

from date import day_add

bot = telebot.TeleBot("1499593962:AAG5ObbcZsycM9O6M9wHD91Xi05b_mPsbTg")


def send_data_to_tg(results, sent_data_tg):
    for disconnection in results:
        if disconnection not in sent_data_tg:
            bot.send_message(1340073704, disconnection)
            sent_data_tg.append(disconnection)
    return sent_data_tg

def check_disconnection(results):

    for disconnection in results:
        tomorrow = day_add()[0]
        three_days = day_add[1]
        week = day_add()[2]

        if disconnection["disconn-start-date"] == f'{tomorrow[0]}.{tomorrow[1]}.{tomorow[2]}' and 