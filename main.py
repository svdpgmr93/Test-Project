import telebot
from config import TOKEN
import json
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('usd', 'eur', 'rur')
with open('out.txt', 'r') as fr:
    lst = json.load(fr)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Прогноз какой валюты вам интересен', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'usd':
        bot.send_message(message.chat.id, 'Доллар стоит ' + str(lst[0]) + 'при покупке, и ' + str(lst[1]) + ' при продаже')
        bot.send_message(message.chat.id, 'Курс какой еще валюты вам интересен', reply_markup=keyboard)
    elif message.text.lower() == 'eur':
        bot.send_message(message.chat.id, 'Евро стоит ' + str(lst[2]) + 'при покупке, и ' + str(lst[3]) + ' при продаже')
        bot.send_message(message.chat.id, 'Курс какой еще валюты вам интересен', reply_markup=keyboard)
    elif message.text.lower() == 'rur':
        bot.send_message(message.chat.id,  'Рубль стоит ' + str(lst[4]) + 'при покупке, и ' + str(lst[5]) + ' при продаже')
        bot.send_message(message.chat.id, 'Курс какой еще валюты вам интересен', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понял, выберите из представленных вариантов', reply_markup=keyboard)


bot.polling()
