import math
# Функции

def f(x):
    return -(1+ math.sin(x))*math.cos(x)
def func(x):
    return (1+ math.sin(x))*math.cos(x)

# Интервал
a = int(input("Введите x :"))
a1 = a
b = int(input("\nВведите y :"))
b1 = b
# Количество вычислений 
N = int(input("Введите количество вычислений целевой функции :"))
N1 = N
Epsilone =  0.001 # float(input("Введите приближение :"))


# Входные данные 
Fib = [1,1]
for i in range(2,N):
    Fib.append(Fib[i-1]+Fib[i-2])
print(Fib)
if N % 2 == 0:
    sign = 1
else:
    sign = -1
x1 = a + (Fib[N-2] * (b-a) - sign*Epsilone) / Fib[N-1]
x2 = a + (Fib[N-2] * (b-a) - sign*Epsilone) / Fib[N-1]

f1 = f(x1)
f2 = f(x2)

j = 1

# Нахождение минимума 
while (j <= (N-1)):
    if ((N - j +1)% 2 == 0):
        sign = 1
    else:
        sign = -1
    
    if (f1 <= f2):
        b = x2 
        x2 = x1
        f2 = f1
        x1 = a + (Fib[N - j - 1] * (b-a) - (sign * Epsilone))/Fib[N-j]
        f1 = f(x1)
        x = x2
    else:
        a = x1 
        x1 = x2
        f1 = f2
        x1 = a + (Fib[N - j - 1] * (b-a) - (sign * Epsilone))/Fib[N-j]
        f2 = f(x2)
        x = x1
    j += 1


# Перезапись входных данных
Fib1 = [1,1]
for i in range(2,N):
    Fib1.append(Fib1[i-1]+Fib1[i-2])
print(Fib1)

if N1 % 2 == 0:
    sign1 = 1
else:
    sign1 = -1

x3 = a1 + (Fib1[N1-2] * (b1-a1) - sign1*Epsilone) / Fib1[N1-1]
x4 = a1 + (Fib1[N1-1] * (b1-a1) - sign1*Epsilone) / Fib1[N1-1]
f3 = func(x3)
f4 = func(x4)
j1 = 1

# Нахождение максимума
while (j1 <= (N1-1)):
    if ((N1 - j1 +1)% 2 == 0):
        sign1 = 1
    else:
        sign1 = -1
    
    if (f3 <= f4):
        b1 = x4 
        x4 = x3
        f4 = f3
        x3 = a + (Fib1[N1 - j1 - 1] * (b1-a1) - (sign1 * Epsilone))/Fib1[N1-j1]
        f3 = func(x3)
        max = x4
    else:
        a1 = x3 
        x3 = x4
        f3 = f4
        x4 = a1 + (Fib1[N1 - j1 - 1] * (b1-a1) - (sign1 * Epsilone))/Fib1[N1-j1]
        f4 = func(x4)
        max = x3
    j1 += 1

print(f'min = {x}\nmax = {max}\nf(min) = {f(x)}\nf(max) = {f(max)}')