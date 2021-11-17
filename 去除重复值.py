#10-26-

import pandas as pd

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
