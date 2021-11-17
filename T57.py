from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

fig=plt.figure()
ax=Axes3D(fig)
colors=['r','g','b']
year=[2016,2017,2018]
for z,color in zip(year,colors):
    x=range(1,13)
    y=10000*np.random.rand(12)
    ax.bar(x,y,zs=z,zdir='y',color=color,alpha=0.8)

ax.set_xlabel('月份')
ax.set_ylabel('年份')
ax.set_zlabel('销量')
ax.set_yticks(year)
plt.show()
