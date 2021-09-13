T=list(input('Введите терминалы:\n'))   
N=list(input('Введите нетерминалы\n'))
print("\nАлфавит терминалов:\n", T)
print("\nАлфавит нетерминалов:\n", N)
list1 = T
list2 = T
list3 = []
while len(list3) <= 10:
    list2 = [i + j for i in list2 for j in list1]
    list3 = list1 + list2
    list2 = list3   

list4 = N
list5 = N
list6 = []
while len(list5) <= 10:
    list5 = [i + j for i in list6 for j in list4]
    list6 = list4 + list5
    list5 = list6  
print("\nТерминалы:\n", list3)
print("\nНетерминалы:\n", list6)

R=[list3[i] + list6[j] for i in range(10) for j in range(10)]
for i in list3:
    R.append(i)
    
L=[list6[i] + list3[j] for i in range(10) for j in range(10)] 
for i in list3:
    L.append(i)
print(R)
print(L)

R=[list3[i] + list6[j] for i in range(10) for j in range(10)]
for i in list3:
    R.append(i)
    
L=[list6[i] + list3[j] for i in range(10) for j in range(10)] 
for i in list3:
    L.append(i)
print(R)
print(L)


P=[]
n=int(input('Количество правил?\n'))
for i in range(n):
    a=[]
    l=input('\nЛевая часть правила:\n')  
    a.append(l)
    rn=int(input('\nСколько правых частей правила?\n'))
    for j in range(rn):
        r=input('\nПравая часть правила:\n')
        a.append(r)
    P.append(a)   
print(P)