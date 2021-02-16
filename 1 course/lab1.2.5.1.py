from math import exp
from math import sqrt

i = int(input('а = '))
j = int(input('b = '))
k = int(input('c = '))

def func(a,b,c):

    # корни для первого уравнения ax^2 + bx - 1.5
    D1 = (b**2) - 4*a*(1.5)
    if D1 > 0:
        x1 =  (-b + sqrt(D1)) / 2*a
        x2 =  (-b - sqrt(D1)) / 2*a
    elif D1 == 0:
        x1,x2 = ((-b)/2*a),0
    else:
        x1,x2 = 0,0

    # корни для второго уравнения 2y^2 - y + c
    D2 = (1**2)-4*2*c
    if D2 > 0:
        y1 =  (1 + sqrt(D2)) / 4
        y2 =  (1 - sqrt(D2)) / 4
    elif D2 == 0:
        y1,y2 = -0.25,0
    else:
        y1,y2 = 0,0


    L = exp(((x1)**2)+((y1)**2)) + exp(((x2)**2)-((y2)**2)) 
    return(L)

U = func(i,j,k)
print(U)