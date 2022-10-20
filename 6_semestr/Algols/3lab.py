"""
Вариант 
Алгоритм Крона
n = 4
m = 20-25
T = 20-35
"""

import os
import time
import numpy as np
import random
# Задание начальных значений
n = 4 # 
m = random.randint(6,15)
T = [random.randint(1,25) for i in range(m)]

# Визуализация процессора
Proc = [[] for i in range(n)]
# Шаг первый
# Генерация случайных индексов процессора
r_ind = [random.randint(0,3) for i in range(m)]
for i in range(m):
    Proc[r_ind[i]].append(T[i])

def out_matric(Proc:list):
    for process in Proc:
        print(process)
print('Матрица процессоров:')
out_matric(Proc)

# Время загрузки каждого проца
k = 0
i = 1
def recursion(last_delt = 0):
    timestamp_sum = [sum(items) for items in Proc]
    print("Суммарное время :",timestamp_sum)
    
    min_Time = min(timestamp_sum)
    index_min_Time = timestamp_sum.index(min_Time)
    max_Time = max(timestamp_sum)    
    index_max_Time = timestamp_sum.index(max_Time)
    print(f'Максимальное время {index_max_Time}|{max_Time}\nМинимальное время {index_min_Time}|{min_Time}')
    
    delt_T = max_Time - min_Time
    print(f"Дельта равна: {delt_T}")
    for el in Proc[index_max_Time]:
        if el < delt_T:
            out = Proc[index_max_Time].pop( Proc[index_max_Time].index(el) )
            Proc[index_min_Time].append(out)
            break

    if delt_T != last_delt:
        return(recursion(delt_T))
    else:
        time.sleep(10)
        os.system("CLS")
        return(Proc)

Proc = recursion()
out_matric(Proc)

print("Суммы процессов: ",list(map(sum,Proc)))

