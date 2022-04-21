"""
Вариант 5
n = 5
m = 6 ... 15
T = 1 ... 25
"""
import numpy as np
import random

m = 5
n = random.randint(6,15)
workload = np.zeros((n,m),dtype=int)

for i in range(n):
    for j in range(m):
        workload[i][j] = random.randint(1,25) 
print("Матрица рабочих процессов :")
print(workload)
sum_row = []
for i in range(n):
    sum = 0
    for j in range(m):
        sum += workload[i][j]
    sum_row.append(sum)
    sum = 0
print(f"Суммы строк: {sum_row}")

timeless_row = sum_row.copy()
timeless_row.sort()
I = []

for i in range(len(sum_row)):
    rindex = 0
    for j in range(len(timeless_row)):
        if sum_row[i] == timeless_row[j]:
            rindex = j
            break
    I.append(rindex)
print(f"Индексы в зависимости от уравнения : {I}")

workload_sorted = []

for i in range(len(I)):
    workload_sorted.append(workload[I[i]])

print("Новая матрица:")
print(np.array(workload_sorted))

process_table = np.zeros((n,m),dtype=int)

for i in range(n):
    min_in_row = min(workload_sorted[i])
    for j in range(m):
        if workload_sorted[i][j] == min_in_row:
            process_table[i][j] = workload_sorted[i][j]
print("Матрица полученная по шагу 2:")
print(process_table)

sum_of_col = []
for i in range(m):
    sum = 0
    for j in range(n):
        sum += process_table[j][i]
    sum_of_col.append(sum) 

print(f"Сумма по столбцам : {sum_of_col}")
print('Результат: {}'.format(max(sum_of_col)))