'''
Вариант 5
n = 4
m = 20-25
T = 20-35
'''
import random

class Thread:
    def __init__(self):
        self._workload = 0 #загруженность
        self._task_bar = list() # 
        self._task = 0 # вес задачи
    
    def update(self):
        self._workload = 0
        i = 0
        while i < len(self._task_bar):
            self._workload += self._task_bar[i]
            i += 1
    @property
    def workload(self):
        return self._workload
    def seperator(self,n):
        divers = self.workload // n
        bizy_threads = [[] for i in range(n)]
        taskbar_for_this = self._task_bar
        taskbar_for_this.reverse()
        now_ind = 0
        while sum(list(map(sum,bizy_threads))) != self.workload:
            len_tasks = len(taskbar_for_this)
            
            if sum(bizy_threads[now_ind]) <= divers:
                taskbar_for_this.reverse()
                bizy_threads[now_ind].append(taskbar_for_this.pop(len_tasks-1))
                taskbar_for_this.reverse()
            else:
                now_ind += 1
            # if len(taskbar_for_this) == 1:
                # bizy_threads[now_ind].append(taskbar_for_this.pop(i))
        return(bizy_threads)
        
    

def main():
    n = 4 # количество активных процессоров
    m = random.randint(20,25) # Генерируем кол-во задач
    processes = [Thread() for i in range(n)]
    tasks = [random.randint(20,35) for i in range(m)]
    print("Сгенерированный список загруженности задач : {}".format(tasks))
    tasks.sort(reverse=True)
    print("Отсортированный список задач : {}".format(tasks))
    print(sum(tasks))

    for i in range(len(tasks)):
        size_of_workloads = [processes[i].workload for i in range(n)]
        minimal_size = min(size_of_workloads)
        for j in range(len(processes)):
            if processes[j].workload == minimal_size:
                processes[j]._task_bar.append(tasks[i])
                processes[j].update()
                break

    size_of_workloads = [processes[i].workload for i in range(n)]
    print(size_of_workloads)

# main()

