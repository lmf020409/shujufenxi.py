from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

fig=plt.figure()
ax=Axes3D(fig)

x=np.arange(-2,2,0.1)
y=np.arange(-2,2,0.1)
x,y=np.meshgrid(x,y)
z=x**2+y**2

ax.plot_surface(x,y,z)
ax.set_xlabel('x轴')
ax.set_ylabel('y轴')
ax.set_zlabel('z轴')
plt.show()