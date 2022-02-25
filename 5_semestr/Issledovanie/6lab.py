from cvxopt.modeling import variable, op
import time
start = time.time()
c= [1,4,2,1,3,\
    6,2,3,5,1,\
    2,3,5,1,4]

x = variable(len(c), 'x')

z=(c[0]*x[0] + c[1]*x[1] +c[2]* x[2] +c[3]*x[3] + c[4]*x[4] \
    +c[5]* x[5] +c[6]*x[6] + c[7]*x[7] + c[8]* x[8] + c[9]*x[9] \
    + c[10]*x[10]+ c[11]*x[11] + c[12]*x[12] + c[13]*x[13] + c[14]*x[14])
a = [300, 250,200]
b = [160,120,140,200,130]
# Проходим по строкам
eq1 = (x[0] + x[1] +x[2] + x[3] + x[4] <= a[0])
eq2 = (x[5] + x[6] +x[7] + x[8] + x[9]<= a[1])
eq3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= a[2])
# Проходим по столбцам
eq4 = (x[0] + x[5] + x[10] == b[0])
eq5 = (x[1] +x[6] + x[11] == b[1])
eq6 = (x[2] + x[7] + x[12] == b[2])
eq7 = (x[3] + x[8] + x[13] == b[3])
eq8 = (x[4] + x[9] + x[14] == b[4])
x_non_negative = (x >= 0)    
problem =op(z,[eq1,eq2,eq3,eq4 ,eq5,eq6, eq7,x_non_negative])
problem.solve(solver='glpk')  
print("Значения X:")
c = 0
for i in x.value:
        print(f"x{c} = {i}")
        c += 1
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print ("Время :")
print(stop - start)