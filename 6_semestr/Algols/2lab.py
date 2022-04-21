"""
Вариант 5
n = 5
m = 6 ... 15
T = 1 ... 25
"""
import numpy as np
import random

n = 5
m = random.randint(6,15)
workload = np.zeros((n,m),dtype=int)

sum_row = []
sum_columns = []

for i in range(n):
    for j in range(m):
        workload[i][j] = random.randint(1,25) 

for i in range(n):
    sum = 0
    for j in range(m):
        sum += workload[i][j]
    sum_columns.append(sum)
    sum = 0

for i in range(m):
    sum = 0
    for j in range(n):
        sum += workload[j][i]
    sum_row.append(sum)
    sum = 0

print(workload,'\n'*2,sum_columns,'\n'*2,sum_row)

# копируем данные для работы с соритровкой
timeless_row = sum_row.copy()
timeless_colums = sum_columns.copy()
# соритровка для I, J согласно неравенству во временных пременных
timeless_row.sort()
timeless_colums.sort(reverse=True)
I = []
J = []
# Получаем индексы для строк
for i in range(len(sum_row)):
    rindex = 0
    for j in range(len(timeless_row)):
        if sum_row[i] == timeless_row[j]:
            rindex = j
            break
    I.append(rindex)
# Получаем индексы для столбцов


for i in range(len(sum_columns)):
    сindex = 0
    for j in range(len(timeless_colums)):
        if sum_columns[i] == timeless_colums[j]:
            сindex = j
            break
    J.append(rindex)

print(I,J)

