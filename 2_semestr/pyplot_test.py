import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,2*np.pi+0.1,0.1)
y = np.cos(x)
fig = plt.figure()
plt.plot(x,y)

plt.title('Cos')
plt.ylabel('Y')
plt.xlabel('X')
plt.text(0.1,3,'Текст',fontsize = 14)

# plt.show() - показывает все графики что были созданы , то есть можно 

# Построение диаграмм

s = ['one','two','three','four','five']
x = [1,2,3,4,5]

z = np.random.random(100)
z1 = [10,17,24,30,5]
z2 = [12,14,19,17,11]

# Cтолбчатая диаграмма

fig = plt.figure()
plt.bar(x,z1)
plt.title('bar')

# Гистаграмма
fig = plt.figure()
plt.hist(z)
plt.pie(x,labels=z2)


plt.show()


