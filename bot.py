import telebot 
import random
bot=telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def bot_start(message):
    bot.reply_to(message.chat.id,"hello")
@bot.message_handler(commands=["fact"])
def bot_fact(message):
    fact=["Мусор бросайте в мусорки","Выбрасывайте лампочки,батарейки и градусники в специальные места"]
    bot.reply_to(message.chat.id,random.choice(fact))

bot.polling()
