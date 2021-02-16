'''
12. Дано целое число N . Определить является ли оно четным 
'''
N = int(input('Введите целое число =  '))
M = 5
G = 8
if N % 2 == 0:
    print('\t Число четное')
else:
    print('\t Число нечетное')

if (N > M)and(N > G):
    print(N, '= max')
elif (M > G)and(M > N):
    print(M, '= max')
else:
    print(G, '= max')
