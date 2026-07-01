import telebot

bot = telebot.TeleBot("<bot token>")

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message,
 'Welcome! Here are the commands this bot supports:\n\
/list - list all items\n\
/add - add a new item\n\
/remove - remove an item\n\
')

# Bot logic

bot.polling()