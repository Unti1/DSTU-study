import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt
import random
from math import * 
# последний импорт означает что мы выносим все функции внутри библиотеке math чтобы не писать каждый раз math.функция
# Задание 1

x = np.arange(0,15,0.1)
u = 7
o = 4
y = (1/(o*sqrt(2*np.pi)))*(np.e**-(((x-u)**2)/(o**2)))


fig = plt.figure()
plt.plot(x,y)
plt.title('Математическая функция')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True) # задание сетки
plt.legend('a',loc=2)  # подпись прямых (функций)


# Задание 2

fig = plt.figure()
n = 250
t = np.linspace(0,59,n)
plt.title('Графики белого шума')
for i in range(1,11):
    ax = fig.add_subplot(10,1,i) # i тут это позиция вывода . 10 тут количество табличек 
    ax.plot(t,[random.uniform(-1,1) for i in range(n)])
    ax.grid(True)

# Задание 3

fig = plt.figure()
activities = ['Сон','Активность2','Активность3','Активность4','Учеба'] # можешь добавить больше активностей (ну и лучше переименуй как нравится) но если будешь добавлять не забуть добавть 
time = [5,4,1,1,5] # > вот сюда цифру для какого то параметра
plt.bar(activities,time)
plt.title('Рaспорядок дня')
plt.ylabel('Время , ч.')
plt.xlabel('Наименования активностей')

# Задание 4

xran = np.linspace(-10,10,500)
yran = np.linspace(-10,10,500)
x, y = np.meshgrid(xran,yran) #создание ортоганальной сетки (не спрашивай я сам в душе не ебу что такое ортоганальная сетка и как ее едят)

z = x**2-3*x*y+y**2+x+2*y+5

plt.figure()

plt.contour(x, y, z, [0])
plt.grid(True)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Задание 5

x = np.linspace(-10,10,300)
y = np.linspace(-10,10,300)

# Значения для этого страшного уравнения . Мы просто присваиваем им значения потому что мы рассматриваем точки x,y поэтому эти переменные ну вообще как бы нас трогать не должны ну и пошли они лесом
# Если хочешь , можешь поменять значения для более лучшего вида графика .   
E = 2.0
yl = 6.0
yr = 4.0
xl = 4.0
xr = 6.0

# Само уравнение (хоспаде кто этот моральный урод который ето придумал) 
z = ((((x-xl+np.sqrt( ((x-xl)**2) + (E**2) ) )*(xr-x+np.sqrt( ((xr-x)**2) + (E**2) )))/(4*np.sqrt( ( ((x-xl)**2) + (E**2) ) * ( ((xr-x)**2) + (E**2) ))))*(((y-yl+np.sqrt( ((y-yl)**2) + (E**2) ) )*(yr-y+np.sqrt( ((yr-y)**2) + (E**2) )))/(4*np.sqrt( ( ((y-yl)**2) + (E**2) ) * ( ((yr-y)**2) + (E**2) )))))

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d") # задает область для трехмерного графика 111 == [1,1,1]
ax.plot(x,y,z,label='Z(x,y)') # собственно строит прямую в трехмерном пространстве
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Функция Z')
plt.show()