import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from mpl_toolkits.mplot3d import Axes3D
# Подключение базы данных
data = pd.read_csv("data.csv")
print(data.columns)
# Задание 1
'''
max = data.select_dtypes(include=['int64','float64']).max()
min = data.select_dtypes(include=['int64','float64']).min()
mean = data.select_dtypes(include=['int64','float64']).drop(['duration_ms'],axis=1).mean()
mid = data.select_dtypes(include=['int64','float64']).median()

print('\nМаксимальные значеия\n',max,'\nМинимальные значения\n',min,'\nСреднее арифмитическое значений\n',mean,'\nМедиана значений\n',mid)

# Задание 2
# данные по конкретной энергичности трека

en = round(random.uniform(0,1),2)# значения должны быть в диапазоне [0,1]
pole = data.loc[data['energy'] <= en,'energy']
sum_fc = pole.sum()
mean_fc = pole.mean()
mean_fc1 = data.loc[data['danceability'] < en,'danceability'].mean()
srt_up = pole.sort_values()
srt_dwn = pole.sort_values(ascending=False)
print('\nДанные по одному полю\n',pole,'\nСумма по группам\n',sum_fc,'\nСортировка по возрастанию\n',srt_up,'\nСортировка по убыванию\n',srt_dwn)

print(mean_fc,mean_fc1)
plt.figure()
plt.bar(['energy','danceability'],[mean_fc,mean_fc1])
plt.title('Гистограмма по среднему значению')
plt.show()
# Страшная версия гистограммы
# mean_fc.hist()

# Задание 3
col = 'duration_ms'
min_for_col = data[col].min()
max_for_col = data[col].max()
mean_for_col = data[col].mean()
mid_for_col = data[col].median()
print('\nМинимальное по столбцу\n',min_for_col,'\nМаксимальное по столбцу\n',max_for_col,'\nСреднее по столбцу\n',mean_for_col,'\nМедиана по столбцу\n',mid_for_col)

# Задание 4
# Сравнение года и популярности музыки, за всё время
list_of_years = [ i for i in range(1928,2020)]
list_of_mean = []
for ye in list_of_years: 
    list_of_mean.append(round(data.loc[data['year'] == ye]['popularity'].mean(),3))
plt.figure()
plt.bar(list_of_years,list_of_mean)
plt.show()
'''
# Задание 5

filt_dat = data[(data['explicit'] == 1)&(data['energy'] > 0.9)&(data['popularity'] <= 30)&(data['popularity'] >= 20)&(data['tempo'] > 200)]
print(filt_dat)
table_sp = filt_dat.pivot_table('danceability','popularity','energy',fill_value=0)
fig = plt.figure(figsize=(15,8))
ax = Axes3D(fig)
print(table_sp)
x_pos = np.arange(table_sp.shape[0])
y_pos = np.arange(table_sp.shape[1])
print(y_pos)
xpos, ypos = np.meshgrid(x_pos, y_pos)
xpos = xpos.flatten()
ypos = ypos.flatten()

zpos=np.zeros(table_sp.shape).flatten()

zpos=np.zeros(table_sp.shape).flatten()
# print(xpos,ypos,zpos)
dx = .8
dy = .8
dz = table_sp.values.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
ax.w_xaxis.set_ticks(x_pos+.4)
ax.w_yaxis.reset_ticks()
ax.w_yaxis.set_ticks(y_pos+.4)

ax.set_xlabel('Энергичность')
ax.set_ylabel('Популярность')
ax.set_zlabel('Танцевальность')

plt.show()


