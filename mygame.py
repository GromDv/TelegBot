import random
import telebot
from telebot import types

# Имя бота для поиска в телеграме: gbpysem9

bot = telebot.TeleBot("токен", parse_mode=None)
# заменить на 5721053114: и AAF7QjMXNL8ESOwdi-irbfgURHVAckzfMTg

spr3 = lambda nums,max: max-1 if nums%max==0 else nums%max - 1
spr2 = lambda nums,max: random.randint(1,max) if nums%max==1 else spr3(nums,max)
spr = lambda nums,max: spr2(nums,max) if nums > max else nums

def numsWord(nums):
    if nums > 10 and nums < 20 :
        return 'конфет'
    elif nums == 1 or nums%10 == 1:
        return 'конфета'
    elif nums > 1 and nums < 5 or nums%10 > 1 and nums%10 < 5:
        return 'конфеты'
    else :
        return 'конфет'

def RnumsWord(nums):
    if nums > 10 and nums < 20 :
        return 'конфет'
    elif nums == 1 or nums%10 == 1:
        return 'конфету'
    elif nums > 1 and nums < 5 or nums%10 > 1 and nums%10 < 5:
        return 'конфеты'
    else :
        return 'конфет'

vsego = 221
maxHod = 28
player = 1
FlagSprav = 0

hiMess = "На столе есть "
hiMess += str(vsego) + " " + numsWord(vsego) + ". "
hiMess += "Играют два игрока делая ход друг за другом. Первый ход определяется случайно. За один ход можно забрать не более чем "
hiMess += str(maxHod) + " " + numsWord(maxHod) + ". "
hiMess += "Все конфеты оппонента достаются сделавшему последний ход.\n\n"


@bot.message_handler(commands = ['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Играть!")
    item2 = types.KeyboardButton("Играть с подсказкой")
    item3 = types.KeyboardButton("Закончить")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,"Сыграем?",reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, hiMess)
    button_message(message)

def send_mess(chat, mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Закончить")
    item2 = types.KeyboardButton("Сначала")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(chat, mess, reply_markup=markup)

def send_final(chat, mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сначала")
    markup.add(item1)
    bot.send_message(chat, mess, reply_markup=markup)

def BotTurn():
    global vsego, maxHod
    if vsego > 0:
        n_bot = spr(vsego, maxHod)
        vsego -= n_bot
    return n_bot


@bot.message_handler(content_types='text')
def message_reply(message):
    global vsego, maxHod, player, FlagSprav

    if message.text=="Сначала":
        send_welcome(message)
    elif message.text=="Играть!":
        send_mess(message.chat.id,'Отлично!')
        vsego = 221
        maxHod = 28

        player = random.randint(1,2)                                    # выбираем кто первый 2 - это бот

        if player == 1:
            FlagSprav = 0
            bot.send_message(message.chat.id, "Вы начинаете! Есть " + str(vsego) + " " + numsWord(vsego) + " Сколько  берете?")
            if FlagSprav == 1:
                bot.send_message(message.chat.id,"подсказка: "+str(spr(vsego, maxHod)))
        else:
            FlagSprav = 0
            bot.send_message(message.chat.id,"Я начинаю!")
            n_bot = BotTurn()
            rep = "Я взял "+str(n_bot)+" "+RnumsWord(n_bot)+". Осталось " + str(vsego) + " " + numsWord(vsego) + ". Сколько берёте?"
            bot.send_message(message.chat.id, rep)
    
    elif message.text=="Играть с подсказкой":
        send_mess(message.chat.id,'Отлично!')
        vsego = 221
        maxHod = 28

        player = random.randint(1,2)   # выбираем кто первый 2 - это бот

        if player == 1:
            FlagSprav = 1
            bot.send_message(message.chat.id, "Вы начинаете! Есть " + str(vsego) + " " + numsWord(vsego) + " Сколько  берете?")
            bot.send_message(message.chat.id,"подсказка: "+str(spr(vsego, maxHod)))
        else:
            FlagSprav = 0
            bot.send_message(message.chat.id,"Я начинаю!")
            n_bot = BotTurn()
            rep = "Я взял "+str(n_bot)+" "+RnumsWord(n_bot)+". Осталось " + str(vsego) + " " + numsWord(vsego) + ". Сколько берёте?"
            bot.send_message(message.chat.id, rep)

    elif message.text=="Нет":
        send_final(message.chat.id,'Жаль... Что ж, успехов!')
    elif message.text=="Закончить":
        send_final(message.chat.id,'Жаль... Что ж, успехов!')

    else:
        nHum = int(message.text)
        if nHum < 1 or nHum > maxHod:
            bot.send_message(message.chat.id,'Есть ' + str(vsego) + " " + numsWord(vsego) + ". Можно брать от 1 до "+str(maxHod) + " " + numsWord(maxHod)+" Повторите ход!")
        else:
            if vsego >= nHum:
                vsego -= nHum
            if vsego == 0:
                bot.send_message(message.chat.id,'Вы выиграли!')
                button_message(message)
            else:
                bot.send_message(message.chat.id,"Мой ход!")
                n_bot = BotTurn()
                bot.send_message(message.chat.id, "Я взял "+str(n_bot)+" "+RnumsWord(n_bot)+".")
                if vsego == 0: 
                    bot.send_message(message.chat.id,'Я выиграл!')
                    button_message(message)
                else:
                    rep = "Осталось " + str(vsego) + " " + numsWord(vsego) + ". Сколько берёте?"
                    bot.send_message(message.chat.id, rep)
                    if FlagSprav == 1:
                        bot.send_message(message.chat.id,"подсказка: "+str(spr(vsego, maxHod)))
                        #send_mess(message.chat.id,"подсказка: "+str(spr(vsego, maxHod)))
        
bot.infinity_polling()
