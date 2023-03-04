import gpt
import keys
import telebot

# a = gpt.Gpt()
# a.gpt('Куда поехать путешествовать по Росии?')

bot = telebot.TeleBot(keys.telegram_key)

@bot.message_handler(content_types=['text'])
def sender(message):
    gpt_obj = gpt.Gpt()
    bot.send_message(message.chat.id, gpt_obj.gpt(message.text))

bot.polling(none_stop=True)