from math import sin
import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure()

# 存放所有顶点的标注信息
annotations = []

# 绘制顶点并创建标注信息
xx = np.arange(0, 4*np.pi, 0.5)
for x in xx:
    y = sin(x)
    # 依次绘制正弦曲线上的每个顶点
    point, = plt.plot(x, y, 'bD', markersize=5)
    # 为每个顶点创建隐藏的文本标注
    # 参数xy表示标注箭头指向的位置，xytext表示文本起始坐标
    # 参数arrowprops表示箭头样式
    # 参数bbox表示标注文本的背景色以及边框样式
    annot = plt.annotate('x=%f,y=%f'%(x,y),
                           xy=(x+0.1, y+0.03), xycoords='data',
                           xytext=(x-2, y+0.2), textcoords='data',
                           arrowprops={'arrowstyle':'->',
                                  'connectionstyle':"arc3,rad=0.5"},
                           bbox={'boxstyle':'round',
                                  'facecolor':'r',
                                  'alpha':0.2},
                           visible=False
                         )
    annotations.append([point, annot])
 
def onMouseMove(event):
    changed = False
    # 遍历所有顶点，检查鼠标当前位置是否与某个顶点足够接近
    # 把足够接近的顶点的标注设置为可见，其他顶点的标注不可见
    for point, annotation in annotations:
        visible = (point.contains(event)[0] == True)
        if visible != annotation.get_visible():
            annotation.set_visible(visible)
            changed = True
    if changed:
        # 只在某顶点标注的可见性发生改变之后才更新画布
        plt.draw()

# 响应并处理鼠标移动事件 
fig.canvas.mpl_connect('motion_notify_event', onMouseMove)
 
plt.show()
