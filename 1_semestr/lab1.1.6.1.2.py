import math
n = int(input('Введите число повторения суммы:'))
x = int(input('Введите число X:'))
i = 1
sum = 0
x = [(x+(math.cos(i*x)))/(2**i) for i in range(n)]
print(x)
for i in x:
    sum = sum + i
print(sum)