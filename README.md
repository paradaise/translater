# translater
tg bot translater on python telebot 

using google-translate library Translator
if u wonna run:
$ pip install googletrans
(https://pypi.org/project/googletrans/)
$ python bot.py
__________________________________________
Переводит 100 плюс языков,сурс язык детектит автоматически.Так же добавлен файл(languages.txt) для удобств с сокращениями языков,изнчально был словарь, его можно получить так:
from googletrans import LANGUAGES

for lang_code, lang_name in LANGUAGES.items():
    print(f'{lang_code}: {lang_name}')
