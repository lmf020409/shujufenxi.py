import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

a = 2
x = np.random.randn(a)
y = np.random.randn(a)

b = 20
xb = np.random.randn(b)
yb = np.random.randn(b)

plt.scatter(x,y,c='r',marker='>')
plt.scatter(xb,yb,c='b',marker='*')
plt.legend(['数据A'],['数据B'])
plt.show()