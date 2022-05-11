import cv2
from threading import Thread
import time
import telebot

FLAG = False
token = input("enter token")


# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот записи видео.')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text#.strip()
    if text == 'go':
        bot.send_message(message.chat.id, 'видео пошло :)')

    elif text == 'end':
        bot.send_message(message.chat.id, 'видео записано')

