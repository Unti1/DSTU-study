import pandas as pd

status= ['q0','q1','s2','s3','q4','s5','s6']
way_a = ['q1','s2','s3','s2','s5','q4','q3']
way_b = ['q4','q4','s5','s3','q1','s3','q5']
#status=['q0','q1','s2','s3','q4','q5','q6','q7']
#zero_way=['q1','s2','s3','s3','q5','s2','s2','s3']
#one_way=['q4','q1','s2','s2','q6','q1','q5','q6']

def remove_odd_status(s, z, o):
    """Удалить недостижимые вершины"""
    for v in s:
        if v not in z and v not in o and v != 'q0':
            index=s.index(v)
            st=s[:index]+s[index+1:]
            ze=z[:index]+z[index+1:]
            on=o[:index]+o[index+1:]

    return pd.DataFrame({'status':st,
                         'a':ze,
                         'b':on})

input_data = remove_odd_status(status, way_a, way_b)

def equals_0(data):
    """Определить группы для 0-эквивалентности"""
    q=[]
    s=[]
    for status in data['status']:
        if status[0] == 'q':
            q.append(status)
        elif status[0] == 's':
            s.append(status)
    return [q, s]

equal_0=equals_0(input_data)

def to_minimize(dataframe, groups=equal_0, new_groups=[]):
    """Минимизировать автомат"""
    
    new_groups.append(groups)
    auph=[]
    #цикл по группам 0 эквивалентности
    for group in groups:
        #цикл по каждому состоянию из этой группы
        for status in group:
            new_group=[status] #выделяю новую группу

            #ищу номер группы по 0, чтобы потом можно было понять, входят ли вершины в одну группу
            #нахожу саму вершину
            for num, s in enumerate(dataframe['a']):
                if int(status[-1]) == num:
                    stat_a=s
                    break
            #а тут нахожу группы, в которую она входит
            for num, gr in enumerate(groups):
                if stat_a in gr:
                    number_of_group_by_0=num
                    break

            #ищу номер группы по 1, чтобы потом можно было понять, входят ли вершины в одну группу
            #нахожу саму вершину
            for num, s in enumerate(dataframe['b']):
                if int(status[-1]) == num:
                    stat_b=s
                    break
            #а тут нахожу группы, в которую она входит
            for num, gr in enumerate(groups):
                if stat_b in gr:
                    number_of_group_by_1=num
                    break
            
            #найти первые соответствия
            temp_a={}
            for num, s in enumerate(dataframe['a']):
                if int(status[-1]) == num:
                    temp_a[f'{status[0]}{status[1]}']=s
                    break

            temp_b={}
            for num, s in enumerate(dataframe['b']):
                if int(status[-1]) == num:
                    temp_b[f'{status[0]}{status[1]}']=s
                    break

            #найти индекс для проверки следующих вершин
            for num in range(len(group)):
                if status[-1] == group[num][-1]:
                    i=num
                    break
            #проход по следуюшим состояниям
            for o_status in range(i+1, len(group)):
                
                #проход по столбцу "0"
                for num, s in enumerate(dataframe['a']):
                    if int(group[o_status][-1]) == num:
                        if s in groups[number_of_group_by_0]:
                            temp_a[f'{group[o_status][0]}{num}']=s
                        break

                #проход по столбцу "1"
                for num, s in enumerate(dataframe['b']):
                    if int(group[o_status][-1]) == num:
                        if s in groups[number_of_group_by_1]:
                            temp_b[f'{group[o_status][0]}{num}']=s
                        break
                
            #создаю группу
            for key in temp_a.keys():
                for key1 in temp_b.keys():
                    if key not in new_group and key == key1:
                        new_group.append(key)
            
            #все вместить в один список
            flag=True
            for gr in auph:
                for item in gr:
                    for aaa in new_group:
                        if aaa == item:
                            flag=False
                            break
            if flag == True:    
                auph.append(new_group)

    #
    if len(new_groups) > 1 and new_groups[-1] == new_groups[-2]:
        new_status=[]
        for a in dataframe['status']:
            if len(a)<1: continue
            for b in new_groups[-1]:
                if a in b: new_status.append(b)
        new_a=[]
        for a in dataframe['a']:
            if len(a)<1: continue
            for b in new_groups[-1]:
                if a in b: new_a.append(b)
        new_b=[]
        for a in dataframe['b']:
            if len(a)<1: continue
            for b in new_groups[-1]:
                if a in b: new_b.append(b)

        print(pd.DataFrame({'status':new_status,'a':new_a,'b':new_b}))
        return [j for _ in new_groups for j in _]
    to_minimize(dataframe, auph, new_groups)

to_minimize(input_data)
