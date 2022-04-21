"""
Вариант 5
Алгоритм Крона
n = 4
m = 6 .. 15
T = 1 .. 25
"""

from re import M
import numpy as np
import random
# Задание начальных значений
n = 4
m = random.randint(6,15)
T = [random.randint(1,25) for i in range(m)]

# Визуализация процессора
Proc = [[] for i in range(n)]
# Шаг первый
# Генерация случайных индексов процессора
r_ind = [random.randint(0,3) for i in range(m)]
for i in range(m):
    Proc[r_ind[i]].append(T[i])
# **Дозаполнение
maxx = max([len(process) for process in Proc])

for i in range(n):
    if len(Proc[i]) < maxx:
        for j in range(len(Proc[i]),maxx):
            Proc[i].append(0)
print('Матрица процессоров:')
print(np.array(Proc))

# Время загрузки каждого проца
k = 0
i = 1
while True:
    timestamp_sum = [sum(items) for items in Proc]
    print("Суммарное время :",timestamp_sum)
    
    min_Time = min(timestamp_sum)
    max_Time = max(timestamp_sum)    
    print(f'Максимальное время {max_Time}\nМинимальное время {min_Time}')
    
    delt_T = max_Time - min_Time
    
    if max(Proc[k]) - min(Proc[i]) < delt_T:
        
    else:
        break
            


    print(np.array(Proc))