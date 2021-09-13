from graphviz import Digraph

alf = ['S0','S1','S2']
count = ['a','b']
in_cout = [[['S0','S1','S2'],['S0','S2']],
            [['S0','S1','S2'],['S0','S2']],
            [[],['S0','S2']]]

def visual_graph(alflist,countlist,in_cout_list,filename): 
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

    dot.render(filename, view=True, format="png")

# visual_graph(alf,count,in_cout,'testout/test_graph.gv')
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
    proverka = 1
    for j in in_cout[i]:
        # проверка со значениями в p_vals
        for k in range(len(p_vals_list)):
            if p_vals_list[k] == j:
                if j != []:
                    timeless_list.append([p_list[k]])
                else:
                    timeless_list.append([])
    # print(timeless_list)
    for j in timeless_list:
        if j == []:
            proverka = 0

    if proverka == 1:
        timeless_list.reverse()
        in_cout_list_determ.append(timeless_list)
    proverka = 1

    
print(in_cout_list_determ)
p_list.remove('')
# visual_graph(p_list,count,in_cout_list_determ,'testout/test_graph2.gv')

word = 'bbaab'#str(input())
c_word = word
word = list(word)
pos = 0
end_pos = len(in_cout_list_determ)-1
count.reverse()
while word != []:
    letter = word.pop(0)# Удаляется начальный элемент
    print(word,'|-',letter) 
    for keys in in_cout_list_determ[pos]:
        f_key = keys[0] # форматирует значение 
        key = int(f_key.split('p')[1])
        if letter == count[key]:
            pos = key 
            # print(key)
# print(pos)
# print(end_pos)
if pos == end_pos:
    print(f'Цепочка "{c_word}" допускается')
else:
    print(f'Цепочка " {c_word}" не допускается')
        

