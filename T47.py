import matplotlib.pyplot as plt

month=list(range(1,13))
money=[5.2,2.7,5.8,5.7,7.3,9.2,18.7,15.6,20.5,18.0,7.8,6.9]

for x,y in zip(month,money):
    color='#%02x'%int(y*10)+'6666'
    plt.bar(x,y,color=color,hatch='*',width=0.6,edgecolor='b',linestyle='--',linewidth=1.5)
    plt.text(x-0.3,y+0.2,'%.1f'%y)

plt.xlabel('月份',fontproperties='simhei',fontsize=12)
plt.ylabel('营业额（万元）',fontproperties='simhei',fontsize=12)
plt.title('烧烤店营业',fontproperties='simhei',fontsize=14)
plt.show()