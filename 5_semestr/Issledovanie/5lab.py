# -*- coding: utf-8 -*-
from scipy.optimize import linprog # загрузка библиотеки ЛП
import scipy
import numpy as np

method = "revised simplex" # двухфазный симплекс-метод
item_matrix = [[3,2], # матрица удельных значений ресурсов
               [3,3],
               [2,5]] 
total_count = [273,300,380] # список объёмов ресурсов
ans = [-4, -5] # список коэффициентов функции цели
transpose_matrix = -scipy.transpose(item_matrix)
d=linprog(total_count, transpose_matrix, ans) # поиск решения

def seperator(d,bn):
    l = list(d[0][:-2])
    jnumber = l.index(max(l)) # Номер перевода
    m = []
    for i in range(bn):
        if d[i][jnumber] == 0:
            m.append(0.)
        else:
            m.append(d[i][-1]/d[i][jnumber])
    inumber = m.index(min([x for x in m[1:] if x!=0]))  # Перенести нижний индекс
    s[inumber-1] = jnumber
    r = d[inumber][jnumber]
    d[inumber] /= r
    for i in [x for x in range(bn) if x !=inumber]:
        r = d[i][jnumber]
        d[i] -= r * d[inumber]

print("Значение целевой функции = ", round(d.fun))
for i in range(len(total_count)):
        print(f"Y_{i} =",round(d.x[i],1))