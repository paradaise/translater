import telebot
from googletrans import Translator
from api_tokens import TG_API_TOKEN
from telebot import types

bot = telebot.TeleBot(TG_API_TOKEN)
main_menu = ('📑Контакты','Перевести текст','💸Поддержать')
donation_menu = ('🫰Юмани', '💰СБП', '↩️Назад')

def keyboard(menu):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in menu:
        markup.add(types.KeyboardButton(item))
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    name = message.from_user.first_name
    bot.reply_to(message, f'<i>Привет,<b>{name} AKA {username}</b>!Я бот переводчик.Я умею переводить более чем на 100 языков мира!\nЯ сам понимаю твой исходный язык, поэтому тебе стоит указать для меня только ключ языка состоящий из двух букв,\n так что лови файл в котором есть ключ для каждого языка!</i>', reply_markup=keyboard(main_menu), parse_mode="html")
    document = open('languages.txt','rb')
    bot.send_document(message.chat.id, document)


@bot.message_handler(content_types=['text'])
def get_information(message):
    if message.chat.type == 'private':
        if message.text == '📑Контакты':
            bot.send_message(message.chat.id,'У вас что-то не работает?Или есть предложения о сотрудничестве?Напишите мне!')
            bot.send_message(message.chat.id,'Гоголев Виктор:\n📱Telegram: t.me/wa55up\n🌐Вконтакте: vk.com/yowa55up\n🐙GitHub: github.com/paradaise\n')
        elif message.text == '💸Поддержать':
            bot.send_message(message.chat.id,'💵Вы можете поддержать наш проект,нажав кнопку ниже:', reply_markup = keyboard(donation_menu))
        elif message.text == '🫰Юмани':
            bot.send_message(message.chat.id,'🫰Вы можете поддержать Юмани по ссылке:\nhttps://yoomoney.ru/to/410013032669115')
        elif message.text == '💰СБП':
            bot.send_message(message.chat.id,'💰Вы можете поддержать CБП по ссылке:')
        elif message.text == '↩️Назад':
            bot.send_message(message.chat.id,'↩️Возвращаемся к основному меню', reply_markup = keyboard(main_menu))
        elif message.text == 'Перевести текст':
            bot.send_message(message.chat.id,'<i>Чтобы перевести текст,отправь мне сообщение вида:</i>\n <b>[text to translate] [target lang] \n Пример</b>: Смотря откуда приходит фабрик, смотря сколько дитейлс <b> en</b>', parse_mode="html")
        else:
            target_lang = message.text.split()[-1]
            bot.send_message(message.chat.id, translate_text(message.text[:-2],target_lang))


def translate_text(text,target_lang = 'en'):
    translation = Translator().translate(text,target_lang)
    return translation.text



bot.polling()