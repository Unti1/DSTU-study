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
    print(i)
    for val in in_cout_list[i]:
        print(val)
        if val != '':
            v_lst = list(val)
            for sym in v_lst:
                dot.edge(alflist[i],sym,label=countlist[0],constraint = 'false')             
# print(dot)
dot.render('testout/test_graph.gv', view=True, format="png")