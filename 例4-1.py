import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PlotCancas(FigureCanvas):
    def __init__(selfself,parent=None,width=0,height=0,dpi=100):#避免中文乱码
        mp.rcParams['font.sans-serif']=['SimHei']
        mp.rcParams['axes.unicode_minus']=False

    def bar(self,number,press,title):
        plt.subplot2grid((12,12),(1,2),colspan=12,rowspan=10)
        plt.barh(range(len(number)),number,height=0.3,color='r',alpha=0.8)#alpha：透明度
        plt.yticks(range(len(number)),press)
        plt.xlim(0,100)
        plt.xlabel('比例')
        plt.title(title)

        for x,y in enumerate(number):
            plt.text(y+0.1,x,'%s'%y+'%',va='center')
        plt.show()

number=[9,2,44,1,1,5,11,4,23]
press=['中国水利水电','中国电力','人民邮电','北京大学','华中科技大学','吉林大学','机械工业','清华大学','电子工业']
p = PlotCancas()
p.bar(number,press,"前10名出版社占有比例")








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






#首先要创建数据库、数据表
#从sales表中统计每个出版社销售图书的总价，并保存在一个CSV文件中
#用条状图显示每个出版社销售图书的总价的情况。
import pandas as pd
import sqlalchemy as sa
import matplotlib as mp
import matplotlib.pyplot as plt
import random

#链接数据库
#使用sqlalchemy链接数据库
conn=sa.create_engine("mysql+pymysql://root:123456@localhost:3306/pythondb")
rstable=pd.read_sql_table(table_name='sales_volume_rankings',con=conn)
#查询各出版社与出版的书的其定价
sqlstr="select press,sum(ding_price) as allsum from sales_volume_rankings group by press order by allsum"
rs=pd.read_sql(sql=sqlstr,con=conn)
#写到csv中
rs.to_csv('press.csv',index=False)
df=pd.read_csv('press.csv')
# 读取,并将各出版社分组，用sum函数计算各出版社的总定价
df=pd.read_csv('press.csv')

#绘图，处理中文乱码
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False
number=df['allsum']
press=df['press']

all_colors = list(plt.cm.colors.cnames.keys())
c=random.choices(all_colors,k=len(number))

bar = plt.bar(range(len(number)),number,color=c,alpha=0.8)
plt.xticks(range(len(number)),press)

plt.ylim(0,5000)
plt.ylabel('总价格')
plt.title('出版社')
for b in bar:
    height = b.get_height()
    plt.text(b.get_x()+b.get_width()/2,height+1,'%s'%str(height)+'元',ha="center",va='bottom')
plt.show()


