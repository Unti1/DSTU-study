import numpy as np
from matplotlib import pyplot as plt

# Задание 4


xran = np.linspace(-15,15,500)
yran = np.linspace(-15,15,500)
x, y = np.meshgrid(xran,yran) # создание ортоганальной сетки (не спрашивай я сам в душе не ебу что такое ортоганальная сетка и как ее едят)

z = x**2-3*x*y+y**2+x+2*y+5

plt.figure()

plt.contour(x, y, z, [0])
plt.grid(True)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()
