import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import random

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

#数据的读取
df = pd.read_csv('press.csv',encoding='utf8')

labellist=df['press']
size=df['allsum']

# all_colors = list(plt.cm.colors.cnames.keys())
# c=random.choices(all_colors,k=len(size))
# color=c
#
# explode = [0.05,0,0.05,0,0.05,0,0.05,0,0.05,0]

plt.pie(size,
        # colors=color,
        labels=labellist,
        # explode=explode,
        labeldistance=1.1,
        autopct='%1.1f%%',shadow=True,
        startangle=0,
        pctdistance=0.6)
plt.axis('equal')
plt.title('各出版社其总价格的所占比',fontsize=12)
plt.legend()
plt.show()
