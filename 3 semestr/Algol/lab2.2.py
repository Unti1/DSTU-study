import random

n = 100
i = 0
word = ''
filename = 'sym.txt'
dicEn = tuple('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

#Генератор текста в файле
with open(filename, "w",encoding='utf8') as f:
    while i != n:
        i += 1
        word += random.choice(dicEn)
    print(word,file=f )

word = ''
position = 0
sym = str(input('Введите символ\n'))
s1 = []

with open(filename,"r",encoding='utf8') as f:
    s = list(f.read())
    s.remove('\n')

    for i in range(len(s)):
        if i == position:
            s1.append(sym)
            s1.append(s[i])
        else:
            s1.append(s[i])

with open(filename,'w',encoding='utf8') as f:
    for i in s1:
        word += i
    print(word,file=f)