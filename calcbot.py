import telebot
from telebot import types
import time

# Имя бота для поиска в телеграме: gbpysem9-2

bot = telebot.TeleBot("token", parse_mode=None)
# заменить на 5844258519: + AAH1P_G4oxMj8-OQxBpMmfjeWR1FZYEtE7A

hiMess = "Это калькулятор!"

num1 = 0
mun2 = 0
flag1 = 0
flag2 = 0
CalcComplex = 0

@bot.message_handler(commands = ['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Считать рациональные")
    item2 = types.KeyboardButton("Считать комплексные")
    item3 = types.KeyboardButton("Закончить")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,"Посчитаем?",reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, hiMess)
    button_message(message)

def send_mess(chat, mess):
    markup = types.ReplyKeyboardMarkup(row_width=6,resize_keyboard=True)
    item1 = types.KeyboardButton("+")
    item2 = types.KeyboardButton("-")
    item3 = types.KeyboardButton("*")
    item4 = types.KeyboardButton("/")
    markup.add(item1,item2,item3,item4)
    if CalcComplex == 0:
        item5 = types.KeyboardButton("%")
        item6 = types.KeyboardButton("//")
        markup.add(item5,item6)
    bot.send_message(chat, mess, reply_markup=markup)

def send_mess_nokeyb(chat, mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = " "
    markup.add(item1)
    bot.send_message(chat, mess, reply_markup=markup)

def oper_message(chat, mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Считать рациональные")
    item2 = types.KeyboardButton("Считать комплексные")
    item3 = types.KeyboardButton("Закончить")
    markup.add(item1, item2, item3)
    bot.send_message(chat,mess,reply_markup=markup)

def send_final(chat, mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сначала")
    markup.add(item1)
    bot.send_message(chat, mess, reply_markup=markup)

def log_file(mes, res):
    f = open("log_file.txt", 'a')
    stim = time.localtime()
    logStr = f"{stim.tm_mday}/{stim.tm_mon} {stim.tm_hour}:{stim.tm_min}:{stim.tm_sec} "
    logStr += f"Chat_ID:{mes.chat.id} "
    if CalcComplex == 0:
        logStr += "Рациональные "
    else:
        logStr += "Коплексные "
    logStr += f"OP:{num1}{mes.text}{num2}={res}\n"
    f.write(logStr)
    f.close()
    
@bot.message_handler(content_types='text')
def message_reply(message):
    global num1, num2, flag1, flag2, CalcComplex

    if message.text=="Сначала":
        send_welcome(message)
    elif message.text=="Считать рациональные":
        CalcComplex = 0
        num1 = 0
        num2 = 0
        send_mess_nokeyb(message.chat.id, "Введите первое число: ")
        #bot.send_message(message, "Введите первое число:")
        flag1 = 1
    elif message.text=="Считать комплексные":
        CalcComplex = 1
        num1 = 0
        num2 = 0
        send_mess_nokeyb(message.chat.id, "Введите первое число: ")
        flag1 = 1

    elif message.text=="Нет":
        send_final(message.chat.id,'Успехов!')
    elif message.text=="Закончить":
        send_final(message.chat.id,'Успехов!')
    elif message.text=="+":
        oper_message(message.chat.id, "Сумма = "+ str(num1 + num2))
        log_file(message,str(num1 + num2))
    elif message.text=="-":
        oper_message(message.chat.id, "Разность = "+ str(num1 - num2))
        log_file(message,str(num1 - num2))
    elif message.text=="*":
        oper_message(message.chat.id, "Произведение = "+ str(num1 * num2))
        log_file(message,str(num1 * num2))
    elif message.text=="/":
        oper_message(message.chat.id, "Частное = "+ str(num1 / num2))
        log_file(message,str(num1 / num2))
    elif message.text=="//":
        oper_message(message.chat.id, "Целое частное = "+ str(num1 // num2))
        log_file(message,str(num1 // num2))
    elif message.text=="%":
        oper_message(message.chat.id, "Остаток от деления = "+ str(num1 % num2))
        log_file(message,str(num1 % num2))
        

    else:
        if flag1 == 1:
            if CalcComplex == 0:
                num1 = int(message.text)
            else:
                num1 = complex(message.text)
            send_mess_nokeyb(message.chat.id, "Введите второе число: ")
            flag1 = 0
            flag2 = 1
        elif flag2 == 1:
            if CalcComplex == 0:
                num2 = int(message.text)
            else:
                num2 = complex(message.text)
            send_mess(message.chat.id, "Введите операцию: ")
            flag2 = 0

        
        
bot.infinity_polling()
