# -*- coding: utf-8 -*-

import telegram
from telegram.ext import *

with open('./token.txt') as file:
    token = file.read()

print(token)
my_bot = telegram.Bot(token=token)
my_bot_updater = Updater(my_bot.token)

def listener(bot, update):
    id = update.message.chat_id
    message = update.message.text
    user = update.message.from_user
    print("ID: " + str(id) + " MESSAGE: " + message)
    print(user)


def start(bot, update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot :v")


start_handler = CommandHandler('start', start)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher = my_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)

my_bot_updater.start_polling()
my_bot_updater.idle()

while True:
    pass
