import pandas as pd

# 读写excel
d=pd.read_excel('test.xlsx')
print(d)

d.to_excel('newtest.xlsx',index=False)
dd=pd.read_excel('newtest.xlsx')
print(dd)

d={'省':['湖南省','湖南省','湖南省','湖南省','湖南省'],
   '市':['长沙市','长沙市','长沙市','长沙市','长沙市'],
   '区':['芙蓉区','岳麓区','天心区','开福区','雨花区']}
f=pd.DataFrame(d)
f.to_excel('newtest.xlsx',index=False)
print(f)

# d=pd.read_excel('test.xlsx')
# print(d)
# d.to_excel('newtest.xlsx',index=False)
# dd=pd.read_excel('newtest.xlsx')
# print(dd)
# d={'省':['湖南省','湖南省','湖南省','湖南省','湖南省'],
#    '市':['长沙市','长沙市','长沙市','长沙市','长沙市'],
#    '区':['芙蓉区','岳麓区','天心区','开福区','雨花区']}
# df=pd.DataFrame(d)
# df.to_excel('xxx.xlsx',index=False)
# dd=pd.read_excel('xxx.xlsx')
# print(dd)

#读取csv文件
# data=pd.read_csv('test.csv')
# print(data)

# data.to_csv('newtest.csv',columns=['D','E'],index=False)
# dd= pd.read_csv('newtest.csv')
# print(dd)
# d={'省':['湖南省','湖南省','湖南省','湖南省','湖南省'],
#    '市':['长沙市','长沙市','长沙市','长沙市','长沙市'],
#    '区':['芙蓉区','岳麓区','天心区','开福区','雨花区']}
#
# df=pd.DataFrame(d)
# df.to_csv('xxx.csv',index=False)
# df=pd.read_csv('xxx.csv')
# print(df)

# d=['AAA','BBB','CCC']
# print(d)
# s=pd.Series(d)
# print(s)
# print(s.index)
# print(s.values)
# print(s[1])
#
# i=['i','ii','iii']
# s=pd.Series(d,index=i)
# print(s)
# print(s.index)
# print(s.values)
# print(s['ii'])
# print(s[['ii','iii']])
#
# d={'A':['1','2','3','4','5'],
#    'B':['6','7','8','9','10'],
#    'C':['11','12','13','14','15']}
# print(d)
# df= pd.DataFrame(d)
# print(df)
# i = ['a','b','c','d','e']
# df=pd.DataFrame(d,index=i)
# print(df)
# df=pd.DataFrame(d,columns=['B','C'])
# print(df)
#
# d={'省':['湖南省','湖南省','湖南省','湖南省','湖南省'],
#    '市':['长沙市','长沙市','长沙市','长沙市','长沙市'],
#    '区':['芙蓉区','岳麓区','天心区','开福区','雨花区']}
# df=pd.DataFrame(d)
# print(df)
# df=pd.DataFrame(d,index=i)
# print(df)
# df=pd.DataFrame(d,columns=['市','区','街道'])
# print(df)
