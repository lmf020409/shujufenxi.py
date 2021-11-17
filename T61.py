import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x=np.random.randint(0,40,30)
y=np.random.randint(0,40,30)
z=np.random.randint(0,40,30)

ax=plt.subplot(projection='3d')

for xx,yy,zz in zip(x,y,z):
    color='r'
    if 10<zz<20:
        color='b'
    elif zz>=20:
        color='g'
    ax.scatter(xx,yy,zz,c=color,marker='*',s=160,linewidth=1,edgecolor='b')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_title('三维散点图',fontproperties='simhei',fontsize=20)
plt.show()