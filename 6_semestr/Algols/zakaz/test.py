import re
number = "Афы фф @"
def ru_check(text):
    return bool(re.fullmatch(r'[а-яА-Я#@ ]+', text))
print(ru_check(number))