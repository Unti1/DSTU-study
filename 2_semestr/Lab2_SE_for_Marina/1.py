import numpy as np
from matplotlib import pyplot as plt
# Задание 1

x = np.arange(0,15,0.1)
u = 7
o = 4
y = (1/(o*np.sqrt(2*np.pi)))*(np.e**-(((x-u)**2)/(o**2)))


fig = plt.figure() # создаем фигуру
plt.plot(x,y) # рисуем прямую по точкам
plt.title('Математическая функция') # Задаем название функции
plt.ylabel('Y') # Задаем назавние оси
plt.xlabel('X') # Задаем назавние оси
plt.grid(True) # задание сетки
plt.legend('a',loc=2)  # подпись прямых (функций)
plt.show() # вывод полученного графика(графиков)
