import matplotlib as mp
import matplotlib.pyplot as plt
import random

mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False

number=[9,2,44,1,1,5,11,4,23]
press=['中国水利水电','中国电力','人民邮电','北京大学','华中科技大学','吉林大学','机械工业','清华大学','电子工业']


all_colors = list(plt.cm.colors.cnames.keys())
c=random.choices(all_colors,k=len(number))

bar = plt.bar(range(len(number)),number,color=c,alpha=0.8)
plt.xticks(range(len(number)),press)
plt.ylim(0,100)
plt.ylabel('比例')
plt.title('出版社占比')
for b in bar:
    height = b.get_height()
    plt.text(b.get_x()+b.get_width()/2,height+1,'%s'%str(height)+'%',ha="center",va='bottom')
plt.show()