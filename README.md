import telebot
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands = ("start"))
def bot_start(message):
    bot.send_message(message.chat.id, "Привет,я бот,который может угадать какая ягода на фото.")


    @bot.message_handler(commands = ("help"))
def bot_start(message):
    bot.send_message(message.chat.id, "/picture")


@bot.message_handler(content_types=['photo']):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
bot.polling()
