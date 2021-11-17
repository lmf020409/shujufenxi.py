import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

baseP=49
saleP=75

def compute(num):
    x=saleP*(1-0.01*num)
    return x

numbers=list(range(1,31))#顾客购买的数量
ears=[]#保存商场盈利情况
totalCompute=[]#存储顾客消费总金额
saves=[]#用来存储顾客节省的金额

for num in numbers:
    perP=compute(num)
    ears.append(round(num*(perP-baseP),2))
    totalCompute.append(round(num*perP,2))
    saves.append(round(num*(saleP-perP),2))

plt.plot(numbers,ears,label='商场盈利')
plt.plot(numbers,totalCompute,label='顾客总消费')
plt.plot(numbers,saves,label='顾客节省金额')

plt.xlabel('顾客购买数量(件)',fontproperties='simhei')
plt.ylabel('金额（元）',fontproperties='simhei')
plt.title('数量-金额关系图',fontproperties='simhei')

myfont=fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf',size=12)
plt.legend(prop=myfont)

maxEarn=max(ears)
bestNumber=numbers[ears.index(maxEarn)]
print(bestNumber)

plt.scatter([bestNumber],[maxEarn],marker='*',color="red",s=120)
plt.annotate(xy=(bestNumber,maxEarn),
             xytext=(bestNumber-1,maxEarn+200),
             s=str(maxEarn),
             arrowprops=dict(arrowstyle='->'))
plt.show()

