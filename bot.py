# -*- coding: utf-8 -*-

import telegram
from telegram.ext import *

with open('./token.txt') as file:
    token = file.read()

print(token)
my_bot = telegram.Bot(token=token)
my_bot_updater = Updater(my_bot.token)

def start(bot, update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot :v")


start_handler = CommandHandler('start', start)

dispatcher = my_bot_updater.dispatcher

dispatcher.add_handler(start_handler)

my_bot_updater.start_polling()
my_bot_updater.idle()

while True:
    pass
