import matplotlib.pyplot as plt

# 存储鼠标依次经过的位置
x = []
y = []

def onMouseClick(event):
    if event.button == 1:
        # 单击鼠标左键，绘制新直线
        x.clear()
        y.clear()
        x.append(event.xdata)
        y.append(event.ydata)

def onMouseMove(event):
    x.append(event.xdata)
    y.append(event.ydata)
    if event.button==1 and len(x)>1:
        plt.plot([x[-2],x[-1]], [y[-2],y[-1]], c='r', lw=2)
    event.canvas.draw()
        
# 创建图形
fig = plt.figure()
ax = plt.gca()
plt.xlim(0, 10)
plt.ylim(0, 10)

# 设置响应并处理事件的函数
fig.canvas.mpl_connect('button_press_event', onMouseClick)
fig.canvas.mpl_connect('motion_notify_event', onMouseMove)

plt.show()
