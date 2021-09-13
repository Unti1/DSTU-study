def type_3(gr):
    p = []
    t = 0
    for i in gr:
        a = i[i.find('>')+1 :]
        if a.find('|') == -1:
            if a.islower():
                p.append(1)
            elif a == 'E':
                p.append(0)
            elif a[0].islower() and a[1].isupper():   # праволинейная
                p.append(2)
            elif a[0].isupper() and a[1].islower():   # леволинейная
                p.append(3)
            else:
                p.append(0)
        else:
            d = a.split('|')
            for j in d:
                if j.islower():
                    p.append(1)
                elif j == 'E':
                    p.append(0)
                elif j[0].islower() and j[1].isupper():   # праволинейная
                    p.append(2)
                elif j[0].isupper() and j[1].islower():   # леволинейная
                    p.append(3)
                else:
                    p.append(0)
    print('p ',p)
    if (1 in set(p)) and (2 in set(p)) and (0 not in set(p)):
        print('грамматика типа 3, праволинейная')
    elif (1 in set(p)) and (3 in set(p)) and (0 not in set(p)):
        print('грамматика типа 3, леволинейная')
    else:
        return t 
        

def type_1(gr):
    p = []
    t = 0
    for i in gr:
        a = i[i.find('>')+1 :]
        if a.find('|') == -1:
            if len(i[:i.find('-')]) <= len(a):
                p.append(1)
            else:
                p.append(0)
        else:
            d = a.split('|')
            for j in d:
                if len(i[:i.find('-')]) <= len(j):
                    p.append(1)
                else:
                    p.append(0)
    if set(p) == {1}:
        print('грамматика типа 1')
    else:
        return t
'----------------------------------------------------------------------------------------------------------------------------------------'
'''
# ввод грамматик
# S->aaS|B|E
# B->b
'''
gr = ['S->Ca|Ba','C->c','B->E']

# проверка на тип
k = 1
for i in gr:
    if i[:i.find('-')].isupper():          # левая часть до '->' проверяется на нетерминальность
        #print('тип 2/3 или 0/1')
        pass
    else:
        #print('тип 0 или 1')
        k = 0

if k == 0:
    t = type_1(gr)
    if t == 0:
        print('грамматика типа 0')
else:
    t = type_3(gr)
    if t == 0:
        print('грамматика типа 2')

        



