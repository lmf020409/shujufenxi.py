#10-26-

import pandas as pd

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
