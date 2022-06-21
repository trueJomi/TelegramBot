import telebot

bot= telebot.TeleBot("5364652689:AAHgxorkubuh9il4p-7GEomVgt6YJZI0CCI")


@bot.message_handler(commands=["help","start"])

def enviar(message):
    bot.reply_to(message, "Que onda")

bot.polling()