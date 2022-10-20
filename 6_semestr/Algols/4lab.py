"""
Вариант 5
Алгоритм Крона
n = 4
m = 20-25
T = 20-35
"""
import os
import time
import numpy as np
import random
from _1lab import Thread

# Задание начальных значений

n = 2 # количество активных процессоров
m = random.randint(20,25) # Генерируем кол-во задач
threads = [Thread() for i in range(n)]
tasks = [random.randint(20,35) for i in range(m)]
tasks.sort(reverse=True)
print("Сгенерированный список загруженности задач : {}".format(tasks))

def process_generate(threads,n,m,tasks):
    for i in range(len(tasks)):
        size_of_workloads = [threads[i].workload for i in range(n)]
        minimal_size = min(size_of_workloads)
        for j in range(len(threads)):
            if threads[j].workload == minimal_size:
                threads[j]._task_bar.append(tasks[i])
                threads[j].update()
                break
    size_of_workloads = [threads[i].workload for i in range(n)]
    return(threads)

N = 2
n_processors = [[Thread() for i in range(n)] for i in range(N)]
now_proc = process_generate(threads,n,m,tasks)
counter = 1
print("1 этап:")
for proc in now_proc:
    print("Задачи:",proc._task_bar," = ",sum(proc._task_bar))
print("2 этап:")
for proc in now_proc:
    n_threds_in_now_proc = proc.seperator(n)
    print("Процессор " + str(counter))
    for lst in n_threds_in_now_proc:
        print("Распределенные задачи: ",lst," = ", sum(lst))
        
    counter += 1

    