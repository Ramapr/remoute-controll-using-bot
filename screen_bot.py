# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import telebot
import os

##############
# CONSTS
token = input('input token\n').rstrip()
PATH = os.path.abspath(os.getcwd())
print(PATH)
captures = {}
##############

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот для калибровки. Отправь номер от 1 до 3 для фото.')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text.strip()
    if text.isnumeric():
        photo_id = int(text)
        if photo_id not in [1, 2, 3]:
            bot.send_message(message.chat.id, 'поддерживаются цифры от 1 до 3')
        else:
            vid = cv2.VideoCapture(0)
            ret, frame = vid.read()
            captures[photo_id] = frame
            print(frame.shape)
            #with open(os.path.join(PATH, 'shot_%d.npy') % photo_id, 'wb') as f:
            #    np.save(f, frame)
            # ---------
            #uncoment this
            cv2.imwrite('shot_%d.jpg' % photo_id, frame)
            #---------
            #if photo_id not in captures.keys():
            bot.send_message(message.chat.id, 'take shot for photo id' + text)
            bot.send_photo(message.chat.id, photo=open('shot_%d.jpg' % photo_id, 'rb'))

# Получение сообщений от юзера
# @bot.message_handler(commands=["calc"])
# def handle_calculus(message):
#     if len(captures) == 3:
#         bot.send_message(message.chat.id, 'расчет положения людей через модель')
#     else:
#         bot.send_message(message.chat.id, 'нет фото')

# Запускаем бота
bot.polling(none_stop=True, interval=0)
