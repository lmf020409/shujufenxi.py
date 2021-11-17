import random
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

# 每月支出数据
data = {
    '蔬菜': [1350, 1500, 1330, 1550, 900, 1400, 980, 1100, 1370, 1250, 1000, 1100],
    '水果': [400, 600, 655, 700, 750, 800, 850, 900, 950, 900, 820, 568],
    '肉类': [500, 354, 456, 400, 500, 600, 350, 450, 480, 580, 658, 590],
    '日用': [1100, 1400, 1200, 1250, 1450, 1350, 1300, 1250, 1150, 950, 850, 1252],
    '衣服': [650, 3500, 0, 2550, 1300, 500, 600, 0, 0, 1300, 0, 900],
    '旅游': [4000, 1800, 0, 0, 0, 0, 0, 0, 0, 4000, 0, 0],
    '随礼': [0, 4000, 0, 600, 1000, 800, 1200, 0, 900, 500, 450, 750]
}
dataLength = len(data['蔬菜'])  # 数据长度
# angles数组把圆周等分为dataLength份
angles = np.linspace(0,  # 数组第一个数据
                     2 * np.pi,  # 数组最后一个数据
                     dataLength,  # 数组中数据数量
                     endpoint=False)  # 不包含终点
markers = '*v^Do'
for col in data.keys():
    # 使用随机颜色和标记符号
    color = f'#{random.randint(0, 0xffffff):06x}'
    plt.polar(angles, data[col], color=color, marker=random.choice(markers), label=col)

# 设置角度网格标签
month = ['{}月'.format(i) for i in range(1, 13)]
plt.thetagrids(angles * 180 / np.pi, month)

plt.legend()
plt.show()