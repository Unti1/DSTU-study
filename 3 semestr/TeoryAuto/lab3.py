from graphviz import Digraph

alf = ['S0','S1','S2']
count = ['a','b']
in_cout = [[['S0','S1','S2'],['S0','S2']],
            [['S0','S1','S2'],['S0','S2']],
            [[],['S0','S2']]]

def visual_graph(alflist,countlist,in_cout_list): 
    dot = Digraph()
    for i in range(len(alflist)):
        dot.node(alflist[i],alflist[i])

    # Построение графов 
    for i in range(len(alflist)):
        for j in range(len(in_cout_list[i])):
            val = in_cout_list[i][j]
            if (val != [])and(val != ''):
                for sym in val:
                    dot.edge(alflist[i],sym,label=countlist[j],constraint = 'true')             

    dot.render('testout/test_graph.gv', view=True, format="png")

# visual_graph(alf,count,in_cout)
# Детерминирование 

p_vals_list = []
p_list = []
in_cout_list_determ = []

for i in range(len(in_cout)):
    for val in in_cout[i]: 
        if (val not in p_vals_list):
            p_vals_list.append(val)

for p in range(len(p_vals_list)):
    if p_vals_list[p] != []:
        p_list.append(f'p{p}')
    else:
        p_list.append('')

for i in range(len(in_cout)):
    # print(in_cout_list[i])
    timeless_list = []
    for j in in_cout[i]:
        # проверка со значениями в p_vals
        for k in range(len(p_vals_list)):
            if p_vals_list[k] == j:
                if j != []:
                    timeless_list.append([p_list[k]])
                else:
                    timeless_list.append([])
    in_cout_list_determ.append(timeless_list)
print(in_cout_list_determ)
p_list.remove('')

visual_graph(p_list,count,in_cout_list_determ)


