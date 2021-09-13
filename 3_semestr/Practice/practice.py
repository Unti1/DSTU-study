# Python Version : 3.8
import math
from matplotlib import pyplot as plt
import numpy as np
# Математические функции
# на заметку - можно добавить интерфейс и адаптивную функцию ввода функций пользователя 
    


def f(x):
    return -((x-2)*math.cos(x))
def func(x):
    return (x-2)*math.cos(x)
print("Исходные данные")
# Интервал
a = 1 #int(input("Введите a : "))
a1 = a
b = 8 #int(input("Введите b : "))
b1 = b
# Количество вычислений
N = 10 #int(input("Введите количество вычислений целевой функции : "))
N1 = N
Epsilone =  0.0001 # float(input("Введите приближение :"))
print("Введите приближение Epsilone : ",Epsilone)
'''
#График функции
ox = np.linspace(a,b,100)
oy = []
for value in ox:
    oy.append(f(value))
fig = plt.figure()
plt.plot(ox,oy)
plt.grid(True)
ax = fig.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.show()
fig.savefig('figure.png',dpi = 100)
'''


# Входные данные
Fib = [1,1]

for i in range(2,N+1):
    Fib.append(Fib[i-1]+Fib[i-2])
print(Fib)

if N % 2 == 0:
    sign = 1
else:
    sign = -1

x1 = a + ((Fib[N-2] * (b-a) - sign*Epsilone)/Fib[N])
x2 = a + ((Fib[N-1]*(b-a) + sign*Epsilone)/Fib[N])

f1 = f(x1)
f2 = f(x2)

j = 1

# Нахождение максимума
while (j <= (N-1)):

    if ((N - j + 1)% 2 == 0):
        sign = 1
    else:
        sign = -1
    
    if (f1 <= f2):
        b = x2 
        x2 = x1
        f2 = f1
        x1 = a + ((Fib[N - j - 1]*(b-a)-sign * Epsilone)/Fib[N-j+1])
        f1 = f(x1)
        x = x2
    else:
        a = x1 
        x1 = x2
        f1 = f2
        x2 = a + ((Fib[N - j] * (b-a) + sign * Epsilone)/Fib[N-j+1])
        f2 = f(x2)
        x = x1
    j += 1



# Перезапись(дублирование) входных данных
print("Нахождение максимума")
Fib1 = [1,1]
for i in range(2,N+1):
    Fib1.append(Fib1[i-1]+Fib1[i-2])
print(Fib1)

if N1 % 2 == 0:
    sign1 = 1
else:
    sign1 = -1

x3 = a1 + ((Fib1[N1-2]* (b1-a1) - sign1*Epsilone) / Fib1[N1])
x4 = a1 + ((Fib1[N1-1]* (b1-a1) + sign1*Epsilone) / Fib1[N1])
print(x3)
print(x4)
f3 = func(x3)
f4 = func(x4)
j1 = 1

# Нахождение максимума
while (j1 <= (N1-1)):
    if ((N1 - j1 + 1)% 2 == 0):
        sign1 = 1
    else:
        sign1 = -1
    
    if (f3 <= f4):
        b1 = x4
        x4 = x3
        f4 = f3
        x3 = a1 + ((Fib1[N1 - j1 - 1] * (b1-a1) - sign1 * Epsilone)/Fib1[N1-j1+1])
        f3 = func(x3)
        max = x4

    else:
        a1 = x3 
        x3 = x4
        f3 = f4
        x4 = a1 + ((Fib1[N1 - j1] * (b1-a1) + sign1 * Epsilone)/Fib1[N1-j1+1])
        f4 = func(x4)
        max = x3

    j1 += 1

print(f'Результаты оптимизации\nmin = {round(x,4)}\nmax = {round(max,4)}\nf(min) = {round(f(x),4)}\nf(max) = {round(f(max),4)}')
