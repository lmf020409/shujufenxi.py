import matplotlib.pyplot as plt

with open('phone.txt') as fp:
    for line in fp:
        x,y,s=map(int,line.split(','))
        if s<40:
            color='r'
        elif s<70:
            color='b'
        else:
            color='s'
        plt.scatter(x,y,s=s*3,c=color,marker='*')

plt.xlabel('长度坐标',fontproperties='simhei',fontsize=12)
plt.xlabel('宽\n度\n坐\n标',fontproperties='simhei',fontsize=12,ratation='horizontal')
plt.title('手机信号强度',fontproperties='simhei',fontsize=20)
plt.show()