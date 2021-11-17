import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

d={'月份':[1,2,3,4,5,6,7,8,9,10,11,12],
   '男装':[51,32,58,57,30,46,38,38,40,53,58,50],
   '女装':[70,30,48,73,82,80,43,25,30,49,79,60],
   '餐饮':[60,40,46,50,57,76,70,33,70,61,49,45],
   '化妆品':[110,75,130,80,83,95,87,89,96,88,86,89],
   '金银首饰':[143,100,89,90,78,129,100,97,108,152,96,87]}

df=pd.DataFrame(d)
print(df)
df.plot(x='月份',kind='bar')

plt.xlabel('月份',fontproperties='simhei',fontsize=12)
plt.ylabel('营业额（万元）',fontproperties='simhei',fontsize=12)
font=fm.FontProperties(fname=r'c:\Windows\fonts\stkaiti.ttf')
plt.legend(prop=font)
plt.show()