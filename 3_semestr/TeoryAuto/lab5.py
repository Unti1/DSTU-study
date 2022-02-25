from graphviz import Digraph

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
print(table['a']['q0'])
filename = 'minimize.png'
table = table.loc[table.index != 'q0']
print(table)
dot = Digraph()
for nod in table.index:
    dot.node(nod,nod)

for start in table.index:
    print(start)
    for labe11 in table.columns:
        print(labe11)
        dot.edge(start , table[labe11][start] ,label=labe11,constraint = 'true')
dot.render(filename, view=True, format="png")

