import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()

x = np.arange(0, 4*np.pi, 0.3)
y = np.sin(x)
ax.plot(x, y, 'r-*', picker=5)

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print('顶点编号：{}\n坐标：{}'.format(ind[0], points))

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
