
import telebot

token = '5527786697:AAFWyd3wzsUT7YTFu5HE049B5h-_UF8ImTU'
Vik = 18

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, 'Hello!')
    bot.send_message(message.chat.id, 'enter your age')


  

bot.polling(non_stop = True, interval=0)
