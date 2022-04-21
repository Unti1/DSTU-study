import pandas as pd
import re

data = pd.read_json("db.json")
print(data.columns)
print(data.mean())

def ru_check(text):
    return bool(re.fullmatch(r'[а-яА-Я#@ ]+', text))

def clear_text_post(text):
    reg = re.compile('[^a-zA-Zа-яА-Я0-9 ]')
    reg = reg.sub('',text)
    reg = re.sub(r'club+\d{8}','',reg)
    return(reg)

for item in data['posts']:
    print("Весь текст на русском ? Ответ:",ru_check(item['text']))
    print(f"Изначальный текст:\nТекст очиценный от хэш-тегов и обращений: ",clear_text_post(item['text']))

