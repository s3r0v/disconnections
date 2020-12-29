import telebot
bot = telebot.TeleBot('1499593962:AAG5ObbcZsycM9O6M9wHD91Xi05b_mPsbTg')

@bot.message_handler()
def send_data(message):
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")