import matplotlib as mp
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False

df=pd.read_csv('chengji.csv')
x=df['keming']
y=df['fenshu']
plt.plot(x,y,linewidth=3,color='r',marker='o',markerfacecolor='blue',markersize=8)

plt.xlabel('课程名')
plt.ylabel('分数')
plt.title('成绩走势图')
plt.grid()
plt.show()