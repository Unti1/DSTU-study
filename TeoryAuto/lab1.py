# Ввод количество символов алфовита


count = int(input('Введите количество символов алфовита: '))
dic = []


# Заполнение значений для алфовита


while len(dic) != count:
    word = str(input(f'\n Введите значение для {len(dic) + 1} символа \n'))
    while word in dic:
        print('Ошибка !\n Данное слово уже находится в словаре ! Введите другое\n')
        word = str(input(f'\n Введите значение для {len(dic) + 1} символа \n'))
    dic.append(word)
print(dic)


# Нахождение номера по слову (+ проверка на наличие символа в словаре)


word = str(input('Введите слово для того чтобы узнать его номер:\n'))
n = len(dic) #Число букв в словаре
k = len(word) #Число букв в слове
N = 0 #Для подсчета номера
r = [] #Для соотношения буквы с позицией в словаре 
count = 0 # Переменная счетчик

for i in list(word): #Проверка буквы  
    if i not in dic:
        print(f"Ошибка. В словаре нету буквы - '{i}' !\n")
        word = str(input('Введите слово для того чтобы узнать его номер с буквами которые прописаны в словаре!\n'))

for i in list(word):
    for j in range(len(dic)):
        if i == dic[j]:
            r.append(j+1)
print(r)

#   Непосредственно вывод номера
while k != 0:
    k -= 1
    N += n**(k)*r[count] 
    count += 1
print(N)


#Вывод слова по номеру 


N = int(input('Введите номер \n'))
n = len(dic)
k = [] 
k1 = ''

while N > len(dic):
    r = 0
    if N % n == 0:
        r = n
        N -= r
        k.append(r)   
        # print(N)
    else:
        while N % n != 0:
            r += 1
            N -= 1
        k.append(r)
    N /= n
    print(N)
k.append(int(N))
k.reverse()

# Преобразования полученной цифры в букву
for i in k:
    k1 += dic[i-1]

print(f'\nЗакодированное слово - "{k1}" ')