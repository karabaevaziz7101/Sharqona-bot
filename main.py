import telebot

# Вставь сюда токен бота
TOKEN =Token for the bot SharqonaShukuhBot @SharqonaShukuhBot has been revoked. New token is:

7770392203:AAFRCvr3UcyZMvqCGSnvRQ8vONqC1jVIoMA
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я работаю ✅")

bot.polling()
