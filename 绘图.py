#10-26

import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.random((5,5)),columns=['a','b','c','d','e'])
p1 = sbn.heatmap(df)
plt.show()