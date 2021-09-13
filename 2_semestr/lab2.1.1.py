import numpy as np
import numpy.random as rand

#1 задание

spisok1 = []
spisok2 = []
massive = np.array([0,2,4,0,2,3,10,0,1,0]) # Простой массив
print(massive.nonzero())
for i in range(len(massive)):
    if massive[i] == 0: 
        spisok1.append(i+1)

matrix = np.array([[0,10,3],[10,2,2],[1,0,3]]) # Матрица

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            spisok2.append((i+1,j+1))

print(f'\n1.Для массива - {massive} , число 0 находится на позициях {spisok1} \n\nДля матрицы  \n{matrix} , число о находится на позициях {spisok2}')

#2 задание

n = int(input("Введите размерность матрицы : \n"))
one_matrix = np.eye(n,n)
print(f'\n2.Матрица размерностью {n}x{n} : \n{one_matrix}\n')

#3 задание

x3_matrix = rand.randint(1,10,(n,n,n))

print(f'3.Матрица размерностью {n}x{n}x{n} : \n{x3_matrix}\n')

#4 задание

vec = np.zeros(n)
print(f'4.Задание одномерного массива \n{vec}\n')

#5 задание
if n < 5:
    n = int(input('Введите число большее или равное 5\n'))

vec_1 = rand.randint(1,10,(n,1))
if vec_1[4][0] != 1:
    vec_1[4][0] = 1
print(f"5.Вектор с 5 элементом 1 \n{vec_1}\n")

#6 задание

n = int(input("Введите числовое значение n\n "))
m = int(input("Введите числовое значение m\n "))
if n > m:
    x = n
    n = m
    m = x
 
vec_2 = rand.randint(n,m+1,(5,1))

print(f'\n6.Вектор с числами от {n} до {m} \n{vec_2}\n')

#7 задание 
n = 3
x2_matrix = rand.randint(1,10,(n,n))
x2_matrix_st = x2_matrix
x2_matrix = x2_matrix.ravel()
x2_matrix = x2_matrix[::-1]
x2_matrix.shape = (n,n)
reversed_matrix = x2_matrix

print(f'7.Исходная матрица \n{x2_matrix_st}\nПеревернутая матрица\n{x2_matrix}\n')

#8 задание 

n = 5
m = 5
r_matrix = np.ones((n,m))
print(f'\n8.Исходная матрица \n{r_matrix}')
for i in range(len(r_matrix[:,0])):
    if r_matrix[i,0] != 1:
        r_matrix[i,0] = 1
for i in range(len(r_matrix[:,-1])):
    if r_matrix[i,-1] != 1:
        r_matrix[i,-1] = 1
for i in range(len(r_matrix[0])):
    if r_matrix[0][i] != 1:
        r_matrix[0][i] = 1
for i in range(len(r_matrix[-1])):
    if r_matrix[-1][i] != 1:
        r_matrix[-1][i] = 1


r_matrix[1:-1,1:-1]=0
print(f'Матрица с рамкой из единиц размерностью {n}x{m}\n{r_matrix}\n')

#9 задание

b = 6
ey_matrix = np.eye(b,b)
n = len(ey_matrix)

spisok3 = []
for g in range(n):
    if g != 0:
        spisok3.append(g) 

for i in range(n):
    if i != 0:# исключение 1ой строчки
        if ey_matrix[i][i-1] != spisok3[i-1]:
            ey_matrix[i][i-1] = spisok3[i-1]
print(f'9. {b}x{b} матрица с 1,2,..,n-1 под диагональю .\n{ey_matrix}\n')
np.diag(np.arange(1,n),k=-1)
#10 задание

n = 5 
shahm = np.zeros((n,n))

for i in range(len(shahm)):
    for j in range(len(shahm[0])):
        if i % 2 == 0:
            if j % 2 == 1:
                shahm[i][j] = 1
        else:
            if j % 2 == 0:
                shahm[i][j] = 1
# или 
    shahm[::2,1::2] = 1
    shahm[1::2,::2] = 1
print(f'10. Матрица {n}x{n} c элементами расположенными в шахмотном порядке \n{shahm}\n')

#11 задание

n = 5
max_matrix = np.random.randint(1,10,(n,n))
print(f'11.Исходная матрица максимальный элемент которой {max_matrix.max()} .\n{max_matrix}\n')
for i in range(len(max_matrix)):
    for j in range(len(max_matrix[0])):
        if max_matrix[i][j] == max_matrix.max():
            max_matrix[i][j] = 0
            break
print(f'Матрица с замененным максимальным элементом на ноль(первым встречающимся)\n`{max_matrix}\n')

#12 задание

# n,m = 1,10
# element = 4
# array = rand.randint(n,m,6)

# vichet_spisok = [i for i in range(n,m)]
# # print(array)
# close_count = False
# for i in range(len(vichet_spisok)):
#     if (array[element] - vichet_spisok[i]) < array[element]:
#         if (array[element] - vichet_spisok[i]) in array:
#             close_count = array[element] - vichet_spisok[i]
#             break
# if close_count == False:
#     close_count = "Нету подходящих ближайших чисел заданных в массиве"
        
# print(f'Ближайшее число к заданному элементу № {element}(считая от 0) - {close_count}')

n,m = -10,11
array = rand.randint(n,m,6)
k = 1
array1 = array - k
array1 = np.absolute(array1)

print(array,array1,array1.argmin())

#13 задание

n = 2
d4_matrix = np.random.randint(1,10,(n,n,n,n))
print(d4_matrix) #НЕ НАДА БУДЕТ КАКАЯ ТО ВАКХАНАЛИЯ
d4_matrix = d4_matrix[:-2].sum()
print(f'13.Сумма последних 2 осей четырехмерного массива равен {d4_matrix}\n')

#14 задание

matrix_with0 = np.array([[0,2,0],[0,0,0],[0,2,0]])
c = 0
spisok4 = []
print(f'14. Из матрицы \n{matrix_with0}\n')
for i in range(len(matrix_with0[0])):
    for num in matrix_with0[:,i]:
        if num == 0:
            c += 1
            print(c)
    if c != 3:
        c = 0
    if c == len(matrix_with0):
        spisok4.append(i)
        c = 0
print(f'Нулевые столбцы находятся в графах {spisok4}\n')

#15 задание

matrix = rand.randint(0,10,(4,4)) 
print(f'15. Исходная матрица \n{matrix}\n')
for i in range(len(matrix)):
    m_sum = (matrix[i].sum())/(len(matrix))
    print(m_sum)
    for j in range(len(matrix[0])):
        matrix[i][j] = matrix[i][j] - m_sum
print(f'Матрица с учетом вычита среднего значения \n{matrix}\n')