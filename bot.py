import DZ_8_Python.config as config
import telebot
from DZ_8_Python.data_export import data_export
from DZ_8_Python.data_print import data_print
import DZ_8_Python.log as lg

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    
    if message.text != 'help':
     lg.logging.info('Пользователь через Бот пытался сделать запрос')  
     bot.send_message(message.chat.id, f'Привет!\nЯ тебя не понимаю.\nВведи: help')
    
    else:
     lg.logging.info('Пользователь через Бот запросил все записи телефонного справочника')   
     message.text == 'help'
     bot.send_message(message.chat.id, f'help - Показать все записи находящиеся в телефонном справочнике')
     data_print(data_export())


print('server start')
bot.infinity_polling()