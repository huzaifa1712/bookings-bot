import telebot
from telebot.types import BotCommand
import os
from bookings import get_bookings

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN, parse_mode=None)

# this shows command suggestions!
bot.set_my_commands([
    BotCommand('start', 'Starts the bot'),
    BotCommand('help', 'Ask for help'),
    BotCommand('bookings', 'List all bookings')
])

@bot.message_handler(commands=['help'])
def help(message):
    print("help")
    bot.send_message(message.chat.id, f'Use this bot to make bookings!\n')
    
# message handler func input only one param = message
    # supports filter of various types
@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    print("From Welcome: -----")
    print(message)
    print("--------")
    bot.reply_to(message, "Hello!")

@bot.message_handler(commands=['bookings'])
def list_bookings(message):
    bookings = get_bookings()
    output = ''

    for idx, val in enumerate(bookings):
        output += f'{idx + 1} : {val}\n'
    
    bot.send_message(message.chat.id, output)


bot.infinity_polling()

