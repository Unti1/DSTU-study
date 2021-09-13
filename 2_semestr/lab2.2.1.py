import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt
import math
import random
from sympy import *

# Задание 1

x = np.arange(0,15,0.1)
u = 7
o = 4
y = (1/(o*math.sqrt(2*np.pi)))*(np.e**-(((x-u)**2)/(o**2)))
# print(y)

fig = plt.figure()
plt.plot(x,y)
plt.title('Ну дал название и дал , чего бубнить то')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.legend('a',loc=2)


# Задание 2

fig = plt.figure()
n = 250
t = np.linspace(0,59,n)
for i in range(1,11):
    ax = fig.add_subplot(10,1,i)
    ax.plot(t,[random.uniform(-1,1) for i in range(n)])
    ax.grid(True)

# Задание 3

fig = plt.figure()
activities = ['Сон','Игры','Пробежка','Тренировка','Учеба']
time = [9,7,1,1,5]
plt.bar(activities,time)
plt.title('Рaспорядок дня')
plt.ylabel('Время в часах')
plt.xlabel('Активности')

# Задание 4

xrange = np.linspace(-10, 10,200)
yrange = np.linspace(-10, 10,200)
x, y = np.meshgrid(xrange,yrange)

# уравнение
z = x**2-3*x*y+y**2+x+2*y+5

plt.figure()
plt.contour(x, y, z, [0])
plt.grid(True)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()

# решение через symppy
# x,y = var('x y')
# plot_implicit(Eq(x**2-3*x*y+y**2+x+2*y+5, 0))

# Задание 5

x = np.linspace(0.1,2,100)
y = np.linspace(0.1,2,100)
x,y = np.meshgrid(x,y)
z = ((np.exp(2*x)-1)*(np.exp(2*y)-1))/((np.exp(2*x)+1)*(np.exp(2*y)+1)) 

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.plot_surface(x,y,z)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Трехмерная страшилка')
plt.show()

 