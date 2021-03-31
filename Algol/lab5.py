import random
import math
from matplotlib import pyplot as plt
import time

n = [100,500,1000,3000,10000]

def Generate_num(n):
    lst = [random.randint(1,1000) for i in range(n)]
    return(lst)


# Линейный поиск
def LinearSearch(lst, val):
    start_time = time.perf_counter()
    for i in range(len(lst)):
        if lst[i] == val:
            end_time = time.perf_counter()
            time_n = round((end_time - start_time),20)
            return (i,time_n)
    return -1

# Поиск с барьером
def BarierSearch (lst, val):
    start_time = time.perf_counter()
    lst.append(val)
    i = 0    
    while lst[i] != val:
        i += 1
    end_time = time.perf_counter()
    time_n = round((end_time - start_time),20)
    if i == len(lst)-1:
        return (-1, time_n)
    else:
        index = i
        return (index, time_n)

# Бинарный поиск
def BinarySearch(lst, val):
    lst.sort()
    start_time = time.perf_counter()
    first = 0
    last = len(lst)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lst[mid] == val:
            index = mid
        else:
            if val < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    end_time = time.perf_counter()
    time_n = round((end_time - start_time),20)
    return (index,time_n)

# поиск элемента и вывод значения 
def func_return(ran):
    
    Bin_Info = []
    Lin_Info = []
    Bar_Info = []
    for n in ran:
        lst = Generate_num(n)
        arg_find = len(lst)//2

        inf = LinearSearch(lst,lst[arg_find])
        Lin_Info.append([n,inf[0],inf[1]])

        inf = BarierSearch(lst,lst[arg_find])
        Bar_Info.append([n,inf[0],inf[1]])
        
        lst = Generate_num(n)
        inf = BinarySearch(lst,lst[arg_find])
        Bin_Info.append([n,inf[0],inf[1]])

    data = (Lin_Info,Bar_Info,Bin_Info)
    return data

data_of_algols = func_return(n)
print(data_of_algols)

# Вывод графиков
def img_output(data):
    yrange = []
    xrange = []
    fig = plt.figure(figsize=(16,9),dpi= 80)
    name_methods = ['Линейный поиск','Поиск с барьером','Бинарный поиск']
    for method in range(len(data)):
        for item in data[method]:
            xrange.append(item[0])
            yrange.append(item[2])
            
        ax = fig.add_subplot(3,1,method+1)
        ax.plot(xrange,yrange)
        plt.ylabel('Доля секунды') 
        plt.xlabel(name_methods[method]) 
        xrange = []
        yrange = []
    plt.show()
    return

img_output(data_of_algols)
