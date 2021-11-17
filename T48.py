import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

d={'男性':[450,800,200],
   '女性':[150,100,300]}
df=pd.DataFrame(d)
df.plot(kind='bar')
plt.xticks([0,1,2],
           (['从不闯红灯','跟别人闯红灯','带头闯红灯']),
           fontproperties='simhei',fontsize=12,
           rotation=20)
plt.yticks(list(df['男性'].values)+list(df['女性'].values))
plt.ylabel('人数',fontproperties='simhei',fontsize=12)
plt.title('过马路',fontproperties='simhei',fontsize=14)
font=fm.FontProperties(fname=r'c:\Windows\fonts\stkaiti.ttf')
plt.legend(prop=font)
plt.show()