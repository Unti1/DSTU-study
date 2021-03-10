import random
import time

elements = (500, 1000, 3000, 5000, 10000)

# генератор для чисел
def generator_of_nums(n):
        nums = []
        i = 0
        while i != n:
            nums.append(random.randint(1,100000))
            i += 1 
        return nums

# Декоратор для времени
def timeline(func):
    def warp(x):
        start_time = time.time()
        value = func(x)
        end_time = time.time()
        time_n = end_time - start_time
        print(f'Время затраченое на выполнение функции: {round(time_n,6)}')
        return value
    return warp


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
        return nums

@timeline
def bubble_sort(nums):  
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
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

@timeline
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

@timeline
def quick_sort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # Это индекс после сводной таблицы, где наши списки разделены
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums

# Вывод алгоритмов
print('\n\tАлгоритм простого включения\n')
for i in elements:
    print(f'\t Размер массива {i}')
    list_of_nums = generator_of_nums(i)
    sorted_list = insertion_sort(list_of_nums)
    for k in (25,50,75):
        list_of_nums[:(len(list_of_nums)//k)] = sorted_list[:(len(list_of_nums)//k)]
        print(f'При заполнении {k}% сортированными элементами')
        insertion_sort(list_of_nums)

print('\n\tАлгоритм прямого выбора\n')
for i in elements:
    print(f'\t Размер массива {i}')
    list_of_nums = generator_of_nums(i)
    sorted_list = selection_sort(list_of_nums)
    for k in (25,50,75):
        list_of_nums[:(len(list_of_nums)//k)] = sorted_list[:(len(list_of_nums)//k)]
        print(f'При заполнении {k}% сортированными элементами')
        selection_sort(list_of_nums)

print('\n\tАлгоритм прямого обмена\n')
for i in elements:
    print(f'\t Размер массива {i}')
    list_of_nums = generator_of_nums(i)
    sorted_list = bubble_sort(list_of_nums)
    for k in (25,50,75):
        list_of_nums[:(len(list_of_nums)//k)] = sorted_list[:(len(list_of_nums)//k)]
        print(f'При заполнении {k}% сортированными элементами')
        bubble_sort(list_of_nums)

print('\n\tАлгоритм быстрой сортировки')
for i in elements:
    print(f'\t Размер массива {i}')
    list_of_nums = generator_of_nums(i)
    sorted_list = quick_sort(list_of_nums)
    for k in (25,50,75):
        list_of_nums[:(len(list_of_nums)//k)] = sorted_list[:(len(list_of_nums)//k)]
        print(f'При заполнении {k}% сортированными элементами')
        bubble_sort(list_of_nums)