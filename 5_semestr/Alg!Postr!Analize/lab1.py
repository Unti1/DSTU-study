import random
import time
import numpy as np
from numba import njit,prange
elements = (10,100,1000,10000,100000,500000)




# генератор для чисел (не люблю ввод ручками)
def generator_of_nums(n):
    nums = []
    i = 0
    while i != n:
        nums.append(random.randint(1,10**8))
        i += 1 
    return np.array(nums)

# Функция для воовода элементов ручками (для 20 элементов в частности)
def self_generator_of_nums(n):
    nums = []
    i = 0
    while i != n:
        nums.append(int(input('Введите цифру: ')))
        i += 1 
    return nums

# Декоратор для времени
def timeline(func):
    def warp(x,*y):
        start_time = time.perf_counter()
        value = func(x)
        end_time = time.perf_counter()
        time_n = end_time - start_time
        print(f'Время затраченое на выполнение функции: {time_n} s.')
        return value
    return warp

# Алгоритм прямого вывода
# @timeline
@njit
def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in prange(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
    return nums

# Алгоритм прямого выбора
# @timeline
@njit
def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in prange(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in prange(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    
# Алгоритм прямого обмена (метод пузырька)
# @timeline
@njit
def bubble_sort(nums):
    #   Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in prange(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return(nums)

#       функция разделения для быстрой сортировки
@njit
def partition(nums, low, high):  
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]
# Алгорим быстрой сортировки
# @timeline
def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    @njit
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


# Пирамидальная сортировка 
    # ВСТРОЕННАЯ ФУНКЦИЯ ДЛЯ ВЕРШИНЫ
@njit
def heapify(nums,heap_size,root_index):
    largest = root_index
    left_child = (2*root_index) + 1
    right_child = (2*root_index) + 2
    # Eсли левый потомок корня - допустимый индекс , а элемент больше,
    # чем текйщий наибольший , обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    # То же самое для правой ветки 
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest],nums[root_index]
        # инициация рекурсии если элемент больше коренного 
        heapify(nums,heap_size,largest)

# CАМ АЛГОРИТМ
# @timeline
@njit
def heap_sort(nums):
    n = len(nums)
    # так называемый MAX HEAP
    for i in prange(n,-1,-1):
        heapify(nums,n,i)
    
    # помещаем MAX_HEAP в конец списка
    for i in prange(n-1,0,-1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 766)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InsertInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.InsertInfo.setGeometry(QtCore.QRect(20, 90, 301, 141))
        self.InsertInfo.setObjectName("InsertInfo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 161, 20))
        self.label.setObjectName("label")
        self.selectionInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.selectionInfo.setGeometry(QtCore.QRect(380, 90, 301, 141))
        self.selectionInfo.setObjectName("selectionInfo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 60, 181, 20))
        self.label_2.setObjectName("label_2")
        self.BubleInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.BubleInfo.setGeometry(QtCore.QRect(20, 290, 301, 151))
        self.BubleInfo.setObjectName("BubleInfo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 121, 20))
        self.label_3.setObjectName("label_3")
        self.QuickInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.QuickInfo.setGeometry(QtCore.QRect(380, 290, 301, 151))
        self.QuickInfo.setObjectName("QuickInfo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 260, 151, 20))
        self.label_4.setObjectName("label_4")
        self.PiramidInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PiramidInfo.setGeometry(QtCore.QRect(220, 490, 301, 141))
        self.PiramidInfo.setObjectName("PiramidInfo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 460, 181, 20))
        self.label_5.setObjectName("label_5")


        self.InsertButton = QtWidgets.QPushButton(self.centralwidget)
        self.InsertButton.setGeometry(QtCore.QRect(190, 50, 93, 28))
        self.InsertButton.setObjectName("InsertButton")
        self.InsertButton.clicked.connect(self.func_return1)
        
        self.SelectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectionButton.setGeometry(QtCore.QRect(570, 50, 93, 28))
        self.SelectionButton.setObjectName("SelectionButton")
        self.SelectionButton.clicked.connect(self.func_return2)

        self.QuickButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.QuickButton_3.setGeometry(QtCore.QRect(560, 254, 93, 28))
        self.QuickButton_3.setObjectName("QuickButton_3")
        self.QuickButton_3.clicked.connect(self.func_return4)
        self.BubbleButton = QtWidgets.QPushButton(self.centralwidget)
        self.BubbleButton.setGeometry(QtCore.QRect(188, 253, 93, 28))
        self.BubbleButton.setObjectName("BubbleButton")

        self.BubbleButton.clicked.connect(self.func_return3)
        self.PiramidButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.PiramidButton_5.setGeometry(QtCore.QRect(410, 450, 93, 28))
        self.PiramidButton_5.setObjectName("PiramidButton_5")
        self.PiramidButton_5.clicked.connect(self.func_return5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InsertInfo.setPlainText(_translate("MainWindow", "10 элементов :\n"
"100 элементов :\n"
"1000 элементов :\n"
"10000 элементов :\n"
"100000 элементов :\n"
"500000 элементов :\n"
"50% сортированных :\n"
"100% сортированных :"))
        self.label.setText(_translate("MainWindow", "Алгоритм прямого вывода"))
        self.selectionInfo.setPlainText(_translate("MainWindow", "10 элементов :\n"
"100 элементов :\n"
"1000 элементов :\n"
"10000 элементов :\n"
"100000 элементов :\n"
"500000 элементов :\n"
"50% сортированных :\n"
"100% сортированных :"))
        self.label_2.setText(_translate("MainWindow", "Алгоритм прямого вывода"))
        self.BubleInfo.setPlainText(_translate("MainWindow", "10 элементов :\n"
"100 элементов :\n"
"1000 элементов :\n"
"10000 элементов :\n"
"100000 элементов :\n"
"500000 элементов :\n"
"50% сортированных :\n"
"100% сортированных :"))
        self.label_3.setText(_translate("MainWindow", "Метод пузырька"))
        self.QuickInfo.setPlainText(_translate("MainWindow", "10 элементов :\n"
"100 элементов :\n"
"1000 элементов :\n"
"10000 элементов :\n"
"100000 элементов :\n"
"500000 элементов :\n"
"50% сортированных :\n"
"100% сортированных :"))
        self.label_4.setText(_translate("MainWindow", "Быстрая сортировка"))
        self.PiramidInfo.setPlainText(_translate("MainWindow", "10 элементов :\n"
"100 элементов :\n"
"1000 элементов :\n"
"10000 элементов :\n"
"100000 элементов :\n"
"500000 элементов :\n"
"50% сортированных :\n"
"100% сортированных :"))
        self.label_5.setText(_translate("MainWindow", "Пирамидальная сортировка"))
        self.InsertButton.setText(_translate("MainWindow", "Запуск"))
        self.SelectionButton.setText(_translate("MainWindow", "Запуск"))
        self.QuickButton_3.setText(_translate("MainWindow", "Запуск"))
        self.BubbleButton.setText(_translate("MainWindow", "Запуск"))
        self.PiramidButton_5.setText(_translate("MainWindow", "Запуск"))





# Функция для вывода алгоритмов
    def func_return1(self):
        _translate = QtCore.QCoreApplication.translate
        time_list = []
        for i in elements:
            list_of_nums = generator_of_nums(i)
            print(f'\t Размер массива чисел {i}')
            time_start = time.perf_counter()
            sorted_list = insertion_sort(list_of_nums)
            time_end = time.perf_counter()
            time_nt = time_end - time_start
            time_list.append(time_nt)

            if i == 500000:
                for proc in (100,50):
                    list_of_nums = generator_of_nums(i)
                    if proc == 0 : 
                        pass
                    else:
                        list_of_nums[:i//proc] = sorted_list[:i//proc]
                    
                    print(f'При заполнении {proc}% несортированными элементами')
                    time_start = time.perf_counter()
                    insertion_sort(list_of_nums)
                    time_end = time.perf_counter()
                    time_nt = time_end - time_start
                    time_list.append(time_nt)
        self.InsertInfo.setPlainText(_translate("MainWindow", f"10 элементов {time_list[0]} :\n"
    f"100 элементов : {time_list[1]} ms\n"
    f"1000 элементов : {time_list[2]} ms\n"
    f"10000 элементов : {time_list[3]} ms\n"
    f"100000 элементов : {time_list[4]} ms\n"
    f"500000 элементов : {time_list[5]} ms\n"
    f"50% сортированных : {time_list[6]} ms\n"
    f"100% сортированных : {time_list[7]} ms"))
    
    def func_return2(self):
        _translate = QtCore.QCoreApplication.translate
        time_list = []
        for i in elements:
            list_of_nums = generator_of_nums(i)
            print(f'\t Размер массива чисел {i}')
            time_start = time.perf_counter()
            selection_sort(list_of_nums)
            sorted_list = list_of_nums
            time_end = time.perf_counter()
            time_nt = time_end - time_start
            time_list.append(time_nt)

            if i == 500000:
                for proc in (100,50):
                    list_of_nums = generator_of_nums(i)
                    if proc == 0 : 
                        pass
                    else:
                        list_of_nums[:i//proc] = sorted_list[:i//proc]
                    
                    print(f'При заполнении {proc}% несортированными элементами')
                    time_start = time.perf_counter()
                    selection_sort(list_of_nums)
                    time_end = time.perf_counter()
                    time_nt = time_end - time_start
                    time_list.append(time_nt)
        self.selectionInfo.setPlainText(_translate("MainWindow", f"10 элементов {time_list[0]} :\n"
    f"100 элементов : {time_list[1]} ms\n"
    f"1000 элементов : {time_list[2]} ms\n"
    f"10000 элементов : {time_list[3]} ms\n"
    f"100000 элементов : {time_list[4]} ms\n"
    f"500000 элементов : {time_list[5]} ms\n"
    f"50% сортированных : {time_list[6]} ms\n"
    f"100% сортированных : {time_list[7]} ms"))
    
    def func_return3(self):
        _translate = QtCore.QCoreApplication.translate
        time_list = []
        for i in elements:
            list_of_nums = generator_of_nums(i)
            print(f'\t Размер массива чисел {i}')
            time_start = time.perf_counter()
            sorted_list = bubble_sort(list_of_nums)
            time_end = time.perf_counter()
            time_nt = time_end - time_start
            time_list.append(time_nt)

            if i == 500000:
                for proc in (100,50):
                    list_of_nums = generator_of_nums(i)
                    if proc == 0 : 
                        pass
                    else:
                        list_of_nums[:i//proc] = sorted_list[:i//proc]
                    
                    print(f'При заполнении {proc}% несортированными элементами')
                    time_start = time.perf_counter()
                    bubble_sort(list_of_nums)
                    time_end = time.perf_counter()
                    time_nt = time_end - time_start
                    time_list.append(time_nt)
        self.BubleInfo.setPlainText(_translate("MainWindow", f"10 элементов {time_list[0]} :\n"
    f"100 элементов : {time_list[1]} ms\n"
    f"1000 элементов : {time_list[2]} ms\n"
    f"10000 элементов : {time_list[3]} ms\n"
    f"100000 элементов : {time_list[4]} ms\n"
    f"500000 элементов : {time_list[5]} ms\n"
    f"50% сортированных : {time_list[6]} ms\n"
    f"100% сортированных : {time_list[7]} ms"))
    
    def func_return4(self):
        _translate = QtCore.QCoreApplication.translate
        time_list = []
        for i in elements:
            list_of_nums = generator_of_nums(i)
            print(f'\t Размер массива чисел {i}')
            time_start = time.perf_counter()
            quick_sort(list_of_nums)
            sorted_list = list_of_nums
            time_end = time.perf_counter()
            time_nt = time_end - time_start
            time_list.append(time_nt)

            if i == 500000:
                for proc in (0,50):
                    list_of_nums = generator_of_nums(i)
                    if proc == 0 : 
                        pass
                    else:
                        list_of_nums[:i//proc] = sorted_list[:i//proc]
                    
                    print(f'При заполнении {proc}% несортированными элементами')
                    time_start = time.perf_counter()
                    quick_sort(list_of_nums)
                    time_end = time.perf_counter()
                    time_nt = time_end - time_start
                    time_list.append(time_nt)
        self.QuickInfo.setPlainText(_translate("MainWindow", f"10 элементов {time_list[0]} :\n"
    f"100 элементов : {time_list[1]} ms\n"
    f"1000 элементов : {time_list[2]} ms\n"
    f"10000 элементов : {time_list[3]} ms\n"
    f"100000 элементов : {time_list[4]} ms\n"
    f"500000 элементов : {time_list[5]} ms\n"
    f"50% сортированных : {time_list[6]} ms\n"
    f"100% сортированных : {time_list[7]} ms"))

    def func_return5(self):
        _translate = QtCore.QCoreApplication.translate
        time_list = []
        for i in elements:
            list_of_nums = generator_of_nums(i)
            print(f'\t Размер массива чисел {i}')
            time_start = time.perf_counter()
            heap_sort(list_of_nums)
            sorted_list = list_of_nums
            time_end = time.perf_counter()
            time_nt = time_end - time_start
            time_list.append(time_nt)

            if i == 500000:
                for proc in (100,50):
                    list_of_nums = generator_of_nums(i)
                    if proc == 0 : 
                        pass
                    else:
                        list_of_nums[:i//proc] = sorted_list[:i//proc]
                    
                    print(f'При заполнении {proc}% несортированными элементами')
                    time_start = time.perf_counter()
                    heap_sort(list_of_nums)
                    time_end = time.perf_counter()
                    time_nt = time_end - time_start
                    time_list.append(time_nt)
        self.PiramidInfo.setPlainText(_translate("MainWindow", f"10 элементов: {time_list[0]} ms\n"
    f"100 элементов : {time_list[1]} ms\n"
    f"1000 элементов : {time_list[2]} ms\n"
    f"10000 элементов : {time_list[3]} ms\n"
    f"100000 элементов : {time_list[4]} ms\n"
    f"500000 элементов : {time_list[5]} ms\n"
    f"50% сортированных : {time_list[6]} ms\n"
    f"100% сортированных : {time_list[7]} ms"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)ё
    MainWindow.show()
    sys.exit(app.exec_())












