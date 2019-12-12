import telebot
from telebot import types
bot = telebot.TeleBot('858886330:AAG-hH4z3LRZ7Bf6_ZEuUCXrWY4koLUwOPE');


@bot.message_handler(regexp="ага лол")
def handle_message(message):
	bot.send_message(message.from_user.id, "пиздец ты самый умный нахуй")
	pass

@bot.message_handler(regexp="/start@cjcfnm_cerf_bot")
def handle_message(message):
	bot.send_message(message.from_user.id, "хуярт")
	pass	
@bot.message_handler(regexp="/start")
def handle_message(message):
	bot.send_message(message.from_user.id, "хуярт")
	pass		
	
@bot.message_handler(regexp="лол")
def handle_message(message):
	bot.send_message(message.from_user.id, "лол у тебя в штанах")
	pass
	
@bot.message_handler(regexp="как дела")
def handle_message(message):
	bot.send_message(message.from_user.id, "нормально")
	pass
@bot.message_handler(regexp="скучаю")
def handle_message(message):
	bot.send_message(message.from_user.id, "о, я тоже по тебе скучаю, друг")
	pass
	
@bot.message_handler(regexp="ору")
def handle_message(message):
	bot.reply_to(message, "ахах")
	pass
#def handle_messages(messages):
#	for message in messages:
		# Do something with the message
#		bot.reply_to(message, 'ага')
#
#bot.set_update_listener(handle_messages)	
	
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if (message.text == "привет") or (message.text == "приветики") or (message.text == "дарова") or (message.text == "хелоу") or (message.text == "Хай") or (message.text == "Приветик"):
		bot.reply_to(message, "бомжур епта)")
	elif message.text == "ага":
			bot.send_message(message.from_user.id, "ага у тебя в штанах")
	elif message.text == "/help":
			bot.send_message(message.from_user.id, "иди нахуй")
	else:
			bot.send_message(message.from_user.id, "я тебя не понимаю. тэгай /help.")


			

bot.polling(none_stop=True, interval=0)