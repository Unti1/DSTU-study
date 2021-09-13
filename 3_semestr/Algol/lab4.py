import random
import time

elements = (20, 500, 1000, 3000, 5000, 10000)




# генератор для чисел (не люблю ввод ручками)
def generator_of_nums(n):
    nums = []
    i = 0
    while i != n:
        nums.append(random.randint(1,10**8))
        i += 1 
    return nums

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
        start_time = time.time()
        value = func(x)
        end_time = time.time()
        time_n = end_time - start_time
        print(f'Время затраченое на выполнение функции: {round(time_n,12)} s.')
        return value
    return warp

# Алгоритм прямого вывода
@timeline
def insertion_sort(nums):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
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
@timeline
def selection_sort(nums):  
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    
# Алгоритм прямого обмена (метод пузырька)
@timeline
def bubble_sort(nums):  
    #   Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return(nums)

#   функция разделения для быстрой сортировки
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
@timeline
def quick_sort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# Функция для вывода алгоритмов
def func_return(n,elements):
    for i in elements:
        list_of_nums = generator_of_nums(i)
        copy_list = list_of_nums
        print(f'\t Размер массива чисел {i}')
        # if i == 20 :
        #     list_of_nums = self_generator_of_nums(i)
        # else:
        #     list_of_nums = generator_of_nums(i)
        
        if n == 1:
            sorted_list = insertion_sort(list_of_nums)
        if n == 2:
            selection_sort(list_of_nums)
            sorted_list = list_of_nums
        if n == 3:
            sorted_list = bubble_sort(list_of_nums)
        if n == 4:
            quick_sort(list_of_nums)
            sorted_list = list_of_nums

        for proc in (0,50,100):
            list_of_nums = generator_of_nums(i)
            list_of_nums[:(len(list_of_nums)//proc)] = sorted_list[:(len(list_of_nums)//proc)]
            print(f'При заполнении {proc}% сортированными элементами')
            if n == 1:
                insertion_sort(list_of_nums)
            if n == 2:
                selection_sort(list_of_nums)
            if n == 3:
                bubble_sort(list_of_nums)
            if n == 4:
                quick_sort(list_of_nums)

print('\n\tАлгоритм простого включения\n')
func_return(1,elements)
print('\n\tАлгоритм прямого выбора\n')
func_return(2,elements)
print('\n\tАлгоритм прямого обмена\n')
func_return(3,elements)
print('\n\tАлгоритм быстрой сортировки')
func_return(4,elements)