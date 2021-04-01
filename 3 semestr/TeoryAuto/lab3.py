from graphviz import Digraph

alflist = ['A','B','C']
countlist = ['a','b']
in_cout_list = [['ABC','AC'],
                ['ABC','AC'],
                ['','AC']]

dot = Digraph()
for i in alflist:
    dot.node(i,i)

for i in range(len(alflist)):
    for j in range(len(in_cout_list[i])):
        val = in_cout_list[i][j]
        if val != '':
            v_lst = list(val)
            for sym in v_lst:
                dot.edge(alflist[i],sym,label=countlist[j],constraint = 'true')             

# print(dot)
dot.render('testout/test_graph.gv', view=True, format="png")