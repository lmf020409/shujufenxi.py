#10-26-

import pandas as pd

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

