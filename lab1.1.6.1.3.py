import math
f = 0
x = -4
h = 0.2
while -4 <= x <= 4:
    x += h
    #print('__',x)
    f = (math.cos(x)+ math.sin(x))/(2+x)
print(f)