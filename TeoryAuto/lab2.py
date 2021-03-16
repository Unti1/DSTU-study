import itertools
#1 задание
print("Задание 1 \n")
n = 5
cout = 0
E = ['0','1']
posl = []
for j in range(n):
    for i in itertools.combinations_with_replacement(E,j):
        for e in itertools.permutations(i):
            posl.append(e)

posl = list((set(posl)))
# print(posl)
posl.sort()

#  Форматирования полученных кортежей в строки

word = ''
posl_c = []
for i in posl:
    for j in i:
        word += j
    posl_c.append(word)
    word = ''
print(posl_c)

posl_c2 = []
for i in posl_c:
    if "101" not in i:
      posl_c2.append(i)  
print(posl_c2)

#2 задание
print('Задание 2 \n')

n = 5
cout = 0
E = ['0','1']
posl = []
posl_c = []
for j in range(n):
    for i in itertools.combinations_with_replacement(E,j):
        for e in itertools.permutations(i):
            posl.append(e)
posl = list((set(posl)))

#  Форматирования полученных кортежей в строки и добавление "," при вхождении 1

word = ''
posl_c = []
for i in posl:
    for j in i:
        word += j
        if j == '1':
            word += ','
    posl_c.append(word)
    word = ''
print(posl_c)

posl_c.sort()
print(posl_c)