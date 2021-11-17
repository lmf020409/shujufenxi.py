import pandas as pd
import csv
#按天间隔
tr=pd.date_range('1/1/2021',periods=365,freq='D')
# 按月间隔
# tr=pd.date_range('1/1/2021',periods=12,freq='M')
# #按小时间隔
# tr=pd.date_range('1/1/2021',periods=24,freq='H')
d={'time':tr}
df=pd.DataFrame(d)
print(df)
df.to_csv('day.csv')

# #求出所有的年份
# y=[i.year for i in df['time']]
# print(y)
# print(df['time'].max())#求最大的时间
# print(df['time'].min())#求最小的时间
# #标准化时间
# df=pd.to_datetime('2021 10 21 20:12:10')
# print(df)
# #算时间差
# x=pd.to_datetime('2021 10 21 20:13:50')-pd.to_datetime('2002 05 20 20:38:50')
# print(x)
#计算两周零两天前的所有时间
ft=df['time']-pd.Timedelta(weeks=2,days=2)
print(ft)