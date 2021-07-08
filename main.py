import telebot

bot = telebot.TeleBot('AAGqvomcrkJ5CC6-hSePdZAYURIXS72C6-4')

@bot.message_handler(commands=['start' , 'help'])

def send_welcome(message):
    bot.reply_to(message, f'Привет, мы будем изучать новые слова')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'не понимаю, что это значит')

bot.polling(none_stop=True)