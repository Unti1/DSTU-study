import numpy as np
from matplotlib import pyplot as plt
import random

# Задание 2

fig = plt.figure()
n = 250
t = np.linspace(0,59,n)
for i in range(1,11):
    ax = fig.add_subplot(10,1,i) # i тут это позиция вывода . 10 тут количество табличек (вернее зарание приготовленных мест для i позиции графика)
    ax.plot(t,[random.uniform(-1,1) for i in range(n)])
    ax.grid(True)
plt.show()