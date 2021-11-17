import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False

df=pd.read_csv('chengji.csv')
print(df)

x=df['keming']
y=df['fenshu']

plt.plot(x,y,linewidth=3,color='r',marker='o',markerfacecolor='blue',markersize=8)