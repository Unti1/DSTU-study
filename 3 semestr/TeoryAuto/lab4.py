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
all_lists = [starter_q_list,endless_q_list] # 0-вая эквиваленция

# Удаление узла без вхождений
new_list_ind = []
list_of_q = []
for ind in table.index:
    for val in table.loc[ind]:
        list_of_q.append(val)
for ind in table.index:
    print(ind)
    if (ind in list_of_q)or(ind == 'q0'):
        new_list_ind.append(ind)
    elif ind in endless_q_list:
        endless_q_list.remove(ind)
    elif ind in starter_q_list:
        starter_q_list.remove(ind)

# Сама функций минимизации
def minimization(lys):
    ekviv_list = []
    for index in table.index: