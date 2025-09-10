import telebot
import os

# Get your bot token from environment variable or directly paste it here
BOT_TOKEN = "7495758013:AAEaEqG8Dws02QTVLEgAijHnTT7SuBMyzK8"
bot = telebot.TeleBot(BOT_TOKEN)

# /hi command
@bot.message_handler(commands=['hi'])
def hi_message(message):
    bot.reply_to(message, "Hi!")

# /hello command
@bot.message_handler(commands=['hello'])
def hello_message(message):
    bot.reply_to(message, "Hello!")

# Run the bot
bot.infinity_polling()
