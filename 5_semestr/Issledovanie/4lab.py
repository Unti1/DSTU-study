# Симплекс метод
from pulp import *
import time
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
x5 = LpVariable("x5", lowBound=0)

start = time.time()
problem = LpProblem('0',LpMaximize)
problem += 4*x1 + 5*x2 + 0*x3 + 0*x4 + 0*x5, "Функция цели"
problem += 3*x1+2*x2+1*x3 == 273,"1" 
problem += 3*x1+3*x2+1*x4 == 300, "2"
problem += 2*x1 + 5*x2+1*x5 == 380, "3"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Значение подставленной в функцию:")
print (abs(value(problem.objective)))
stop = time.time()
print ("Время :")
print(stop - start)