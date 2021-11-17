#10-26-

import pandas as pd
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