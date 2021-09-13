import numpy as np
import matplotlib.pyplot as plt


# Задание 5
x = np.linspace(0.1,2,100)
y = np.linspace(0.1,2,100)
x,y = np.meshgrid(x,y)
z = ((np.exp(2*x)-1)*(np.exp(2*y)-1))/((np.exp(2*x)+1)*(np.exp(2*y)+1)) 
print(z)

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.plot_surface(x,y,z)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Z')
plt.show()