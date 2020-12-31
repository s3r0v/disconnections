import telebot
bot = telebot.TeleBot('1499593962:AAG5ObbcZsycM9O6M9wHD91Xi05b_mPsbTg')

def send_data_to_tg(results, sent_data_tg):
	for i in range(len(results)):
		if results[i] not in sent_data_tg:
			bot.send_message(1340073704, results[i])
			sent_data_tg.append(results[i])
	return(sent_data_tg)
