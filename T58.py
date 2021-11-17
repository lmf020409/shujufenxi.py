import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x,y=np.mgrid[-2:2:20j,-2:2:20j]
z=50*np.sin(x+y*2)

ax=plt.subplot(111,projection='3d')

ax.plot_surface(x,y,z,
                rstride=3,
                cstride=2,
                cmap=plt.cm.coolwarm)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_title('三维曲面',fontproperties='simhei',fontsize=24)

plt.show()