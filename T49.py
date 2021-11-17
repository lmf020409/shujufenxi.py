import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

x=np.arange(0,50)
fig=plt.figure(figsize=(6,4))   #设置画布大小
x1=fig.add_subplot(211)    #添加子图x1，211代表2行1列第1个位置
plt.title('子图1')
x1.plot(x,x)

x2=fig.add_subplot(212)     #添加子图x2,212代表2行1列第2个位置
plt.title('子图2')
x2.plot(x,x**2)
plt.show()