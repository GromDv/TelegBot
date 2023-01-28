import random
import telebot
from telebot import types

bot = telebot.TeleBot("token", parse_mode=None)
# заменить на 5844258519: и AAH1P_G4oxMj8-OQxBpMmfjeWR1FZYEtE7A

hiMess = "Это калькулятор!"

@bot.message_handler(commands = ['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Считать")
    item2 = types.KeyboardButton("Закончить")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,"Посчитаем?",reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, hiMess)
    button_message(message)

def send_mess(chat, mess):
    markup = types.ReplyKeyboardMarkup(row_width=5,resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    item6 = types.KeyboardButton("6")
    item7 = types.KeyboardButton("7")
    item8 = types.KeyboardButton("8")
    item9 = types.KeyboardButton("9")
    item10 = types.KeyboardButton("0")
    item11 = types.KeyboardButton("+")
    item12 = types.KeyboardButton("-")
    item13 = types.KeyboardButton("*")
    item14 = types.KeyboardButton("/")
    item15 = types.KeyboardButton("=")
    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
    bot.send_message(chat, mess, reply_markup=markup)

def send_final(chat, mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сначала")
    markup.add(item1)
    bot.send_message(chat, mess, reply_markup=markup)
    
@bot.message_handler(content_types='text')
def message_reply(message):
    global vsego, maxHod, player, FlagSprav

    if message.text=="Сначала":
        send_welcome(message)
    elif message.text=="Считать":
        send_mess(message.chat.id, "Начнем!")

    elif message.text=="Нет":
        send_final(message.chat.id,'Успехов!')
    elif message.text=="Закончить":
        send_final(message.chat.id,'Успехов!')

    else:
        pass
        
bot.infinity_polling()