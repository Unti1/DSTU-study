import random

x = int(input('Предел первого списка : '))
y = int(input('Предел второго списка : '))
k = int(input('K-тый элемент списка : '))

if k > x:
    print('\n Введен индекс выходящий за пределы первого списка \n')
    exit()

A = [random.randint(1,50) for i in range(x+1)]
B = [random.randint(1,50) for i in range(y+1)]
C = A

print('\n',A)
print('\n',B)
print('\n',C)

B.reverse()

for i in range(y+1):
    C.insert(k+1,B[i])

print('\n \n', C)