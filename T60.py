import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import mpl_toolkits.mplot3d

df=pd.DataFrame({'男性':(450,800,200),'女性':(150,100,300)})

ax=plt.subplot(projection='3d')
ax.bar3d([0]*3,range(3),[0]*3,0.1,0.1,df['男性'].values,color='r')
ax.bar3d([1]*3,range(3),[0]*3,0.1,0.1,df['女性'].values,color='b')

ax.set_xticks([0,1])
ax.set_xticklabels(['男性','女性'],fontproperties='simhei')

ax.set_yticks([0,1,2])
ax.set_yticklabels(['从不闯红灯','跟从别人闯红灯','带头闯红灯'],fontproperties='simhei')

ax.set_zlabel('人数',fontproperties='simhei')

plt.show()

