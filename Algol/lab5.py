import random
import math
import matplotlib as plt
import time

n = [100,500,1000,3000,10000]

def Generate_num(n):
    lst = [random.randint(1,1000) for i in range(n)]
    return(lst)



def LinearSearch(lst, val):
    start_time = time.perf_counter()
    for i in range(len(lst)):
        if lst[i] == val:
            end_time = time.perf_counter()
            time_n = round((end_time - start_time),20)
            return (i,time_n)
    return -1


def BarierSearch (a, x):
    start_time = time.perf_counter()
    
    array = [num for num in a]
    array.append(x)
    i = 0
    
    # двигаемся по массиву, пока требуемое значение не будет найдено
    while array[i] != x:
        i += 1
        index
        
    # если уткнулись в барьер, возвращаем -1
    if i == len(array)-1:
        return [-1, time]
    end_time = time.perf_counter()
    time_n = round((end_time - start_time),20)
    return (-1,time_n)


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

def func_return(ran):
    
    Bin_Info = []
    Lin_Info = []
    Bar_Info = []
    for n in ran:
        lst = Generate_num(n)
        arg_find = random.choice(lst)
        inf = BinarySearch(lst,arg_find)
        Bin_Info.append([n,inf[0],inf[1]])
        
        lst = Generate_num(n)
        arg_find = random.choice(lst)
        inf = LinearSearch(lst,arg_find)
        Lin_Info.append([n,inf[0],inf[1]])

        inf = BarierSearch(lst,arg_find)
        Bar_Info.append([n,inf[0],inf[1]])
    data = (Lin_Info,Bar_Info,Bin_Info)
    return data

data_of_algols = func_return(n)
print(data_of_algol)
# def img_output(data):
#     for method in data:
        


# img_output(data_of_algols)