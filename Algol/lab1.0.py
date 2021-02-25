#1
A = [int(input('Введите значение\n')) for i in range(int(input('Сколько элементов будет в множестве ?\n'))) ]

# n = int(input("Сколько элементов будет в множестве ?\n"))
# for i in range(n):
#     A.append(input('Введите знавение\n'))

for i in range(len(A)):
    print(f'{i}\t{A[i]}')

#2

word1 = 'Составить программу определения количества гласных букв'
word2 = 'Организовать программу для задания элементов множества'

array1 = word1.split(' ')
array2 = word2.split(' ')

def comparison(val1,val2):
    array3 = []
    for i in val1:
            if i in val2:
                array3.append(i)
    return(array3)

def nocomparison(val1,val2):
    array3 = []
    for i in val1:
        if i not in val2:
            array3.append(i)
    for i in val2:
        if i not in val1:
            array3.append(i)
    return(array3)


print(comparison(array1,array2))
print(nocomparison(array1,array2))
#3

S = ['a','к','ф','r',2,3,'e']
dicRu = tuple('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФЧЦЧШЩЪЫЬ')
dicEn = tuple('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
A = []
B = []
C = []

for i in S:
    if i in dicRu:
        A.append(i)
    elif i in dicEn:
        B.append(i)
    elif type(i) == int :
        C.append(i)
    else:
        print('Неопознанный словарь')

print(A,B,C)