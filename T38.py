import matplotlib as mp
import matplotlib.pyplot as plt

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

labellist=['好评','中差评']
size=[99,1]
color=['blue','red']
explode = [0.05,0]
plt.pie(size,colors=color,
        labels=labellist,
        explode=explode,
        labeldistance=1.1,
        autopct='%1.1f%%',shadow=False,
        startangle=0,
        pctdistance=0.6)
plt.axis('equal')
plt.title('图书好评率',fontsize=12)
plt.legend()
plt.show()
