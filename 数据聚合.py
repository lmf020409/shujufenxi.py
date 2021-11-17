#10-26-

import pandas as pd

data = {'key': ['a','a','b','c','a'],
        'data': [1,2,3,4,5],
        'data1':[2,4,6,8,10]}

df=pd.DataFrame(data)

dff=df.groupby('key').agg(['max','min','median'])
print(dff)

