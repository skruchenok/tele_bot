import telebot
import token

bot = telebot.TeleBot(token.TOKEN)


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
