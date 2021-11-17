import pandas as pd
import pymysql as pm
import sqlalchemy as sa
import numpy as np
import csv

d={'A':['1','2','3','4','5'],
   'B':['6','7','8','9','10'],
   'C':['11','12','13','14','15']}
df=pd.DataFrame(d)
print(df)
print("*************************************************")
#增加一行数据
df['D']=['10','20','30','40','50']
print(df)
print("*************************************************")
#删除单行数据
df.drop([0],inplace=True)
print(df)
print("*************************************************")
#删除单列数据
df.drop(labels=['A'],axis=1,inplace=True)
print(df)
print("*************************************************")
#删除多行数据
df.drop(range(0,3),axis=0,inplace=True)
print(df)
print("*************************************************")
#修改数据
df['B'][2]='88'
print(df)
#修改列数据
df['C']=['8','8','8','8','8']
print(df)
#查询数据
print(df['A'])
print(df.B)
print(df[0:4])
#查询某个特定的数据‘
print()
print(df['A'][3])
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
df=pd.DataFrame(data)
print(df)
df['A'][0]=np.nan
print(df)
print()
#判断每列有几个空值
print(df.isnull().sum())
#判断每列有几个非空
print(df.notnull().sum())
#含有空值的行整行删除
df.dropna(axis=0,inplace=True)#含有空值的列整列删除:axis=1。
print(df)

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
df=pd.DataFrame(data)
df['A'][0]=np.nan
df['A'][1]=np.nan
df['A'][2]=np.nan
df['A'][3]=np.nan
df['A'][4]=np.nan
df.dropna(how='all',axis=1,inplace=True)  #删除含nan元素所包含的整行
print(df)

#替换None的元素
data = {'A': [1, None, 3, 4, 5],
        'B': [6, 7, 8, None, 10],
        'C':[11,12,None,14,None]}
df=pd.DataFrame(data)
print(df)
df.fillna(0,inplace=True)
print(df)
#按要求替换
data = {'A': [1, None, 3, 4, 5],
        'B': [6, 7, 8, None, 10],
        'C':[11,12,None,14,None]}
df=pd.DataFrame(data)
print(df)
df.fillna({'A':0,'B':1,'C':2},inplace=True)
print(df)




#按天间隔
tr=pd.date_range('1/1/2021',periods=365,freq='D')
# 按月间隔
tr=pd.date_range('1/1/2021',periods=12,freq='M')
#按小时间隔
tr=pd.date_range('1/1/2021',periods=24,freq='H')
d={'time':tr}
df=pd.DataFrame(d)
print(df)
df.to_csv('day.csv')

#求出所有的年份
y=[i.year for i in df['time']]
print(y)
print(df['time'].max())#求最大的时间
print(df['time'].min())#求最小的时间
#标准化时间
df=pd.to_datetime('2021 10 21 20:12:10')
print(df)
#算时间差
x=pd.to_datetime('2021 10 21 20:13:50')-pd.to_datetime('2002 05 20 20:38:50')
print(x)
#计算两周零两天前的所有时间
ft=df['time']-pd.Timedelta(weeks=2,days=2)
print(ft)

#建立数据库链接
# conn=sa.create_engine("mysql+pymysql://root:123456@localhost:3306/pythondb")
# d={'A':['1','2','3','4','5'],
#    'B':['6','7','8','9','10'],
#    'C':['11','12','13','14','15']}
# df=pd.DataFrame(d)
# df.to_sql('to_sql_demo',conn,if_exists='append')
# sqlstr="select * from to_sql_demo"
# rs=pd.read_sql(sql=sqlstr,con=conn)
# print(rs)

# conn=sa.create_engine("mysql+pymysql://root:123456@localhost:3306/pythondb")
# d={'province':['湖南省','湖南省','湖南省','湖南省','湖南省'],
#    'city':['长沙市','长沙市','长沙市','长沙市','长沙市'],
#    'area':['芙蓉区','岳麓区','天心区','开福区','雨花区']}
# df=pd.DataFrame(d)
# df.to_sql('to_sql_test',conn,if_exists='append',index=False)
# sqlstr="select * from to_sql_test"
# rs=pd.read_sql(sql=sqlstr,con=conn)
# print(rs)

# #使用sqlalchemy链接数据库
# conn=sa.create_engine("mysql+pymysql://root:123456@localhost:3306/pythondb")
# rstable=pd.read_sql_table(table_name='sales_volume_rankings',con=conn)
# print(rstable)
# sqlstr="select book_name,press from sales_volume_rankings where book_name like '%%Java%%'"
# rs=pd.read_sql(sql=sqlstr,con=conn)
# print(rs)
# print("**********************************************************************")
# #写到csv中
# rs.to_csv('xxx.csv',index=False)
# df=pd.read_csv('xxx.csv')
# print(df)
# print("**********************************************************************")
# #写到excle中
# rs.to_excel('ttt.xlsx',index=False)
# dd=pd.read_excel('ttt.xlsx')
# print(dd)


#使用pymsql链接数据库
# conn = pm.connect(host="localhost",#服务器参数（服务器名称）
#                   user="root",
#                   passwd="123456",
#                   db="pythondb",#数据库的名称
#                   port=3306,
#                   charset="utf8"
#                 )
# sqlstr="select book_name,press from sales_volume_rankings where book_name like'%Python%'"
# rs=pd.read_sql(sql=sqlstr,con=conn)
# print(rs)



