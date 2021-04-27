import pandas as pd
from graphviz import Digraph
from collections import Counter

table = pd.DataFrame([
    ['q1','q4'],
    ['q2','q4'],
    ['q3','q5'],
    ['q2','q3'],
    ['q5','q1'],
    ['q4','q3'],
    ['q5','q3']
    ],
    columns = ['a','b'],
    index = ['q0','q1','q2','q3','q4','q5','q6']
    )
endless_q_list = ['q2','q3','q5','q6']
starter_q_list = []

# Определение вневершинных узлов
for i in  table.index:
    if i not in endless_q_list:
        starter_q_list.append(i)

# Удаление узла без вхождений
new_list_ind = []
list_of_q = []
for ind in table.index:
    for val in table.loc[ind]:
        list_of_q.append(val)
for ind in table.index:
    # print(ind)
    if (ind in list_of_q)or(ind == 'q0'):
        new_list_ind.append(ind)
    elif ind in endless_q_list:
        endless_q_list.remove(ind)
    elif ind in starter_q_list:
        starter_q_list.remove(ind)

zero_eq = [starter_q_list,endless_q_list] # 0-вая эквиваленция

# Сама функций минимизации
def minimization(lys):
    last_ek_list = lys
    ekviv_list = []
    checker = 0
    for area in lys:# Выбор рабочей области (0-вая эквиваленция) {q0 q1 q4} и {q2 q3 q5}
        # print('Текущая рабочая область',area)
        temp_a = []
        # Проверка по 'a'
        for element in area:
            if table['a'][element] in area:
                temp_a.append(element)
        # print('Найденые схождения по а ',temp_a)    
        # Проверка по 'b'
        temp_b = []
        for element in area:
            if table['b'][element] in area:
                temp_b.append(element)
        # print('Найденые схождения по b ',temp_b)    

        # Выделение новой области
        temp = []
        if (len(temp_a) == 0)and(len(temp_b) == 0):
            # print('0')
            temp = []
        elif len(temp_a) == 0:
            # print('1')
            temp.append(temp_b[0])
        elif len(temp_b) == 0:
            # print('2')
            temp.append(temp_a[0])
        elif len(temp_a) > len(temp_b):
            # print('3')
            for val in temp_a:
                if val in temp_b:
                    temp.append(val)
        elif len(temp_b) > len(temp_a):
            # print('4')
            for val in temp_b:
                if val in temp_a:
                    temp.append(val)
        # print('Создание новой области ',temp)

        # Остаточные области (не отделенные)
        non_eq_list = []
        for element in area:
            if element not in temp:
                non_eq_list.append(element)
        # print('\n')

        if len(temp) != 0:
            ekviv_list.append(temp) # Добавление области в лист эквивалентных
        if len(non_eq_list) != 0:
            ekviv_list.append(non_eq_list) # Добавление области в лист неэквивалентных

    if ekviv_list != last_ek_list:
        checker += 1
    # print(ekviv_list)
    if checker == 0:
        return(ekviv_list)
    else:
        return(minimization(ekviv_list))
    
mini = minimization(zero_eq)
print(mini)

# Работа с новой таблицей 
nq = []
for val in mini:
    leng = len(val)
    if leng <= 1:
        nq.append(val[0])
    else:
        for i in range(leng):
            nq.append(val[i])

non = []
for val in table.index:
    if val not in nq:
        non.append(val)
print(non)

def st_remove(table = pd.DataFrame() ,vals = list()):
    vals = vals
    if len(vals) != 0:
        new_table = table.loc[table.index != vals[0]]
        vals.remove(vals[0])
        return(st_remove(new_table,vals))
    else:
        return(table)
print(st_remove(table,non))

# Визуализация минимизации
def vizual_graph(table):
    filename = 'minimize.png'
    dot = Digraph()
    for nod in table.index:
        dot.node(nod,nod)

    for start in table.index:
        for label in table.columns:
            dot.edge(start , table[label][start] ,label=label,constraint = 'true')
    # dot.render(filename, view=True, format="png")
