#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from datetime import datetime as dt
from orator import DatabaseManager, Model
import telegram
import logging
import yaml

# Load orator config
with open("orator.yml", 'r') as stream:
    config = yaml.load(stream)

# Orator database object
db = DatabaseManager(config['databases'])
Model.set_connection_resolver(db)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

help_text = """Hi !

Commands :

/help           This help message

/register       Register to this bot

/product        Product list

/order          Order Product
Example: /order beton 100

/cart           Product cart

/checkout       Checkout and receive invoice

"""

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text(help_text)

def register(bot, update):
    try:
        is_registered = db.table('backend_user').where('telegram_id', update.message.chat.id).first()

        if is_registered == None:
            users = {
                'username': update.message.chat.username,
                'first_name': update.message.chat.first_name,
                'last_name': update.message.chat.last_name,
                'telegram_id': update.message.chat.id,
                'register_date': update.message.date
            }
            db.table('backend_user').insert(users)
            update.message.reply_text('Register Success.')
        else:
            update.message.reply_text('Already Registered.')
    except:
        print('something wrong, sorry')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text(help_text)

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def unknown(bot, update):
    """Unknown command."""
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def product(bot, update):
    prices = '*Produk* : \n'
    products = db.table('backend_product').get()
    for product in products:
        strings = str(product['id']) + '. ' + product['name'] + ' = ' + str(product['price']) + '\n'
        prices += strings

    bot.send_message(
        chat_id=update.message.chat_id,
        text=prices,
        parse_mode=telegram.ParseMode.MARKDOWN
    )

def search_product(search_string):
    return db.table('backend_product').where('name', 'like', "%" + search_string + "%").first()

def order(bot, update, args):
    if len(args) == 2:
        product_name = args[0]
        quantity = args[1]

        product = search_product(product_name)
        user = db.table('backend_user').where('telegram_id', update.message.chat.id).first()

        if product:
            message = 'Added to cart'
            item_cart = db.table('backend_cart').where('user_id', user['id']).where('product_id', product['id']).first()

            if item_cart == None:
                cart = {
                    'user_id': user['id'],
                    'product_id': product['id'],
                    'quantity': quantity
                }
                db.table('backend_cart').insert(cart)
                message = 'Item added to cart'
            else:
                message = 'Item added to cart, updating the quantity'
                prev_quantity = item_cart['quantity']
                new_quantity = item_cart['quantity'] + int(quantity)
                db.table('backend_cart').where('id', item_cart['id']).update({'quantity': new_quantity})

        else:
            message = 'Product not found'

        bot.send_message(
            chat_id=update.message.chat_id,
            text=message,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
    else:
        message = 'Product is not found or wrong command. Example: /order beton 100'
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message,
            parse_mode=telegram.ParseMode.MARKDOWN
        )

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    with open("telegram.yml", 'r') as stream:
        bot_config = yaml.load(stream)
    updater = Updater(bot_config['token'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("product", product))
    dp.add_handler(CommandHandler("order", order, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # unknown command
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
