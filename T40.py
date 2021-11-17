import matplotlib as mp
import matplotlib.pyplot as plt

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

data=[[100,500,300,400,800,700],[80,150,340,210,500]]
labels = ['工厂A','工厂B']

plt.boxplot(data,labels=labels)
plt.title('工厂AB的年产值')
plt.show()
