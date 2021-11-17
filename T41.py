import pandas as pd
import sqlalchemy as sa
import matplotlib as mp
import matplotlib.pyplot as plt
#链接数据库
#使用sqlalchemy链接数据库
conn=sa.create_engine("mysql+pymysql://root:123456@localhost:3306/pythondb")
#查询各出版社与出版的书的其定价
sqlstr="select press,ding_price from sales_volume_rankings where press='人民邮电出版社' group by press,ding_price"

sqlstr_1="select press,ding_price from sales_volume_rankings where press='电子工业出版社' group by press,ding_price"

rs=pd.read_sql(sql=sqlstr,con=conn)
rs_1=pd.read_sql(sql=sqlstr_1,con=conn)

d1=rs['ding_price']
d2=rs_1['ding_price']

for x in range(len(d1)):
    d1[x]=float(d1[x])
for x in range(len(d2)):
    d2[x]=float(d2[x])

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

# data=[df['ding_price'],df['ding_price']]
data=[d1,d2]
labels = ['人民邮电出版社','电子工业出版社']

plt.boxplot(data,labels=labels)
plt.title('出版社')
plt.show()
