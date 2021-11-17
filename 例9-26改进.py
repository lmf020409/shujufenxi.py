import warnings
import numpy as np
import matplotlib.pyplot as plt

# 忽略警告信息
warnings.filterwarnings("ignore",".*GUI is implemented.*")

# 测试数据
x = np.arange(1, 13)
y = np.random.randint(1, 30, 12)
for i in range(20):
    # 清除当前轴域
    plt.cla()
    # 绘制水平柱状图
    temp = sorted(zip(x,y), key=lambda item:item[1])
    x = [item[0] for item in temp]
    y = [item[1] for item in temp]
    plt.barh(range(1,13), y)
    plt.title('20%02d年'%i, fontproperties='simhei',fontsize=20)
    plt.yticks(range(1,13), list(map(lambda i: '%d月'%i, x)),
               fontproperties='simhei')
    plt.xticks(list(range(0,160,20)))
    for xx, yy in zip(range(1,13),y):
        plt.text(yy+0.1, xx-0.1, str(yy))
    # 暂停0.5秒
    plt.pause(0.5)
    # 更新数据
    y = y+np.random.randint(0, 10, 12)
    
plt.show()
