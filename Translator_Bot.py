import telebot
from translator_word import Translate

# bu bot hozirda mavjud emas !

TOKEN = "6515872200:AAGmVjwBPH7I_om9dDsDXHwFINFFeSqIu50"
translator = telebot.TeleBot(token=TOKEN)
language = 'uz'

@translator.message_handler(commands=['start'])
async def greeting(message):
    greeting_msg = "salom, tarjimon botga xush kelibsz\ntilni o'zgartirish uchun /til buyrug'idan foydalaning (bot hozir o'zbek tilida)"
    translator.reply_to(message,greeting_msg)

@translator.message_handler(commands=['til'])
async def mark_languange(message):
    global language
    if language == "uz":
        language = 'en'
        translator.reply_to(message,"til ingliz tiliga o'zgatirildi")
    elif language == 'en':
        language = 'uz'
        translator.reply_to(message,"til o'zbek tiliga o'zgatirildi")

@translator.message_handler(func=lambda txt: txt.text is not None)
def translate_word(message):
    text =  message.text
    WORDS = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',"'"," "]
    check = True
    for i in text:
        if str(i).lower in WORDS:
            continue
        else:
            check = False
            break
    if check:
        translator.reply_to(message,Translate(text,language))
    else:
        translator.reply_to(message,"please enter a word, not a sticker or anything else")    
translator.polling()