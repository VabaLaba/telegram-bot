import telebot as telebot
from bs4 import BeautifulSoup
import requests
import time
import logging
import telegram
import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram import ChatAction, Bot
from telegram import bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

URL = 'https://www.google.com/search?client=ms-android-xiaomi&ei=OJNoX_bYJY3nsAexz7GICg&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82&gs_lcp=CgZwc3ktYWIQARgBMgUIABCxAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQQzoKCAAQsQMQgwEQQzoHCAAQsQMQQ1D8CVjGHWDLLWgAcAF4AoABiAmIAa4jkgEJMi0zLjYtMy4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


@bot.message_handler (content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message (message.from_user.id, "Привет.")
    elif message.text == "/help":
        bot.send_message (message.from_user.id, "Напиши Привет")
    else:
        bot.send_message (message.from_user.id, "Я тебя не понимаю. Напиши /help.")


updater = Updater(token='866419537:AAGoddwHAT6xgBFtW80Mite_Q778OEe-3K0', use_context=True)
dispatcher = updater.dispatcher



def start(updater, context):

    context.bot.send_message(chat_id=updater.effective_chat.id, text="I'm a bot, please talk to me!")
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)




def main():
    full_page = requests.get (URL, headers=headers)
    soup = BeautifulSoup (full_page.content, 'html.parser')
    convert = soup.findAll ("span",
                            {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})  # it is parsing bitcoin

    print ("real course now is :", convert [0].text)
    time.sleep (3600)
    bot = Bot (token='866419537:AAGoddwHAT6xgBFtW80Mite_Q778OEe-3K0',base_url="https://telegg.ru/orig/bot", )
    updater = Updater(bot=Bot, )
    dispatcher = updater.dispatcher
    updater.start_polling ( )
    updater.idle ( )
if __name__ == '__main__':
    main()



