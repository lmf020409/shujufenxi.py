import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

x=np.arange(1,50)
fig,axes = plt.subplots(2,2)  #创建四个子图，两行两列
#分配画布位置
x1=axes[0,0]
x2=axes[0,1]
x3=axes[1,0]
x4=axes[1,1]

x1.plot(x,x)
x2.plot(x,-x)
x3.plot(x,x**2)
x4.plot(x,np.log(x))

plt.show()