m = int(input("Введите начальное число отсчета : "))
n = int(input("Введите конченое число отсчета : "))
i = 0
sum = 0
if m > n:
    print('Начало интервала не может быть больше конца')
else:
    nums = [m for m in range(n) if m % 2 == 1]
    print(nums)
    for i in nums:
        print(i)
        sum = sum + i
    print(sum)
    
