import numpy as np
from numpy.matrixlib.defmatrix import matrix
import sys


def matrix_generation(n,m,min = 0,max = 100,cout = 1):
    matrixs = []
    if cout-1 != 0:
        for i in cout:
            A = np.random.randint(min,max,(n,m))
            matrixs.append(A)
        return(matrix)
    else:
        A = np.random.randint(min,max,(n,m))
        return(A)

    
def matrix_chain_order(p:list):
    n = len(p) - 1
    m = np.zeros((n,n),dtype="int")
    s = np.zeros((n,n),dtype="int")

    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            m[i,j] = 999999
            for k in range(i,j):
                q = int(m[i,k]+m[k+1,j]+p[i]*p[k+1]*p[j+1])
                print(f"m{i+1,j+1} = m{i+1,k+1}+m{k+1,j+1}+p{i}*p{k+1}*p{j+1} = {q}")
                if q < m[i,j]:
                    m[i,j] = q
                    s[i,j] = k
    return(m,s)

def matrix_multiply(A,B):
    # Вычисление ширины и длины Матриц
    l_A = 0
    for row in A:
        l_A += 1
    l_B = 0
    for row in B:
        l_B += 1
    r_B = len(B[0])
    r_A = len(A[0])

    C = np.zeros((l_A,r_B))

    if l_A != r_B:
        return("Ошибка , матрицы нельзя перемнодить")
    else:
        for i in range(r_A-1):
            for j in range(l_B-1):
                C[i][j] = 0
                for k in range(l_A+1):
                    C[i][j] += A[i][k] + B[k][j]
        return(C)



# MATRIX-CHAIN-ORDER    
# p = [40, 20, 30, 10, 30]
p = [30,35,15,5,10,20,25]

#MATRIX_MULTIPLY
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])

def PrintOptimalParens(s,i,j):
    # print(s)
    if i==j:
        print(f'A[{i}]',end='')
    else:
        print ('(',end='')
        PrintOptimalParens(s,i,s[i][j])
        PrintOptimalParens(s,s[i][j]+1,j)
        print(')',end='')
m = matrix_chain_order(p)[0]
s = matrix_chain_order(p)[1]
print(m)
print(s)
PrintOptimalParens(s,0,len(p)-2)