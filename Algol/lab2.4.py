import random

n = 100 # число букв в строке
N = 50 # количество строк
i = 0
filename = 'sym3.txt'
dicEn = tuple(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# создание текстового файла

with open(filename, "w",encoding='utf8') as f:
    for i in range(N):
        word = ''
        while i != n:
            i += 1
            word += random.choice(dicEn)
        print(word,file=f )

# функция поиска в файле введеной строке

def finder(file_name,num):