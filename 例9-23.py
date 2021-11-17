from itertools import cycle
import matplotlib.pyplot as plt

# 存储鼠标依次单击的位置
x = []
y = []
# 可用颜色和当前颜色
colors = cycle('rgbcmyk')
color = next(colors)

def onMouseClick(event):
    global color
    if event.button == 1:
        # 单击鼠标左键，绘制新直线
        x.append(event.xdata)
        y.append(event.ydata)
        if len(x) > 1:
            plt.plot([x[-2],x[-1]], [y[-2],y[-1]], c=color, lw=2)
        plt.xticks(range(10))
        plt.yticks(range(10))
    elif event.button == 3:
        # 单击鼠标右键，切换颜色
        color = next(colors)
    elif event.button == 2:
        # 单击鼠标中键，删除最后绘制的一个图形
        if ax.lines:
            del ax.lines[-1]
            x.pop()
            y.pop()
    event.canvas.draw()
        
def onClose(event):
    print('closed')

def onClear(event):
    # 按下键盘上的c，清除所有已绘制图形
    if event.key == 'c':
        ax.lines.clear()
        x.clear()
        y.clear()
        # 更新图形画布
        event.canvas.draw()

# 创建图形
fig = plt.figure()
ax = plt.gca()
plt.xticks(range(10))
plt.yticks(range(10))

# 设置响应并处理事件的函数
fig.canvas.mpl_connect('button_press_event', onMouseClick)
fig.canvas.mpl_connect('key_press_event', onClear)
fig.canvas.mpl_connect('close_event', onClose)

plt.show()
