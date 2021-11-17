import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
month = list(range(1,13))
money=[5.2,2.7,5.8,5.7,7.3,9.2,18.7,15.6,20.5,18.0,7.8,6.9]

plt.plot(month,money,'r-.v')
plt.scatter(month,money,c='b',marker='*',s=28)
plt.xlabel('月份',fontproperties='simhei',fontsize=14)
plt.ylabel('营业额',fontproperties='simhei',fontsize=14)
plt.title('烧烤店2019年营业变化趋势图',fontproperties='simhei',fontsize=20)
plt.tight_layout()
plt.show()