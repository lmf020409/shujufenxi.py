import pandas as pd
#数据分组
data = {'key': ['a','a','b','c','a'],
        'data': [1,2,3,4,5],
        'data1':[2,4,6,8,10]}

df=pd.DataFrame(data)
print(df)

dfg = df.groupby(df['key'])

print(dfg)
print(dfg.size())
print(dfg.count())
print(dfg.mean())
print(dfg.max())

for i in dfg:
    print("\n",i)

#数据聚合
data = {'key': ['a','a','b','c','a'],
        'data': [1,2,3,4,5],
        'data1':[2,4,6,8,10]}

df=pd.DataFrame(data)

dff=df.groupby('key').agg(['max','min','median'])
print(dff)


#合并数据
data = {'A': ['A1','A2','A3'],
        'B': ['B1','B2','B3'],
        'C':['C1','C2','C3']}
data1 = {'C': ['C1','C2','C3'],
         'D': ['D1','D2','D3'],
         'E':['E1','E2','E3']}

data2 = {'C': ['D1','D2','D3'],
         'E':['E1','E2','E3'],
         'F':['F1','F2','F3']}

df=pd.DataFrame(data)
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

#纵向
print(pd.concat([df,df1],sort=True))
print()
#横向
print(pd.concat([df,df1],sort=True,axis=1))
#how有三个参数、right右连接outer外连接inner内连接，on合并的键名必须相同
print()
print(pd.merge(df,df1,how='outer',on='C'))
print(df.join(df2,lsuffix='_l',rsuffix='_r'))

#去重复值
#inplace:是否在原数据上进行操作。默认TRUE
#subset：指定需要去重的列名
#keep：表示保存重复数据的哪一条数据，first表示保留第一条，last表示最后一条，False表示重复项数据都不保留，默认first
d={'A':['A1','A1','A3'],
   'B':['B1','B2','B1']}
df = pd.DataFrame(d)
print(df)
df.drop_duplicates('B',inplace=True)
print(df)

# #创建时数据
# data = {'A':['A1','A1','A1','A2','A2'],
#         'B':['B1','B1','B3','B4','B5'],
#         'C':['C1','C2','C3','C4','C5']}
# df=pd.DataFrame(data)
# print(df)
# df.drop_duplicates(subset=['A','B'],inplace=True)
# print(df)


#填充数据
import numpy as np
data = {'A': ['A1',None,'A3'],
        'B': [np.nan,'B2','B3'],
        'C':['C1',np.nan,'C3']}
data1 = {'A': ['A5','A2','D3'],
        'B': ['B1',None,'B4'],
        'C':['C5','C2','C3']}
df=pd.DataFrame(data)
df1=pd.DataFrame(data1)
print(df)
print()
print(df1)
print()
print(df.combine_first(df1))
print(df1.combine_first(df))

#绘图
import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.random((5,5)),columns=['a','b','c','d','e'])
p1 = sbn.heatmap(df)
plt.show()


