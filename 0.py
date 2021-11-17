from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fig=plt.figure()
ax=fig.gca(projection='3d')
theta=np.linspace(-4*np,4*np.pi,100)
z=np.linspace(-4,4,100)*0.3
r=z**4+1

# C:\Users\303\AppData\Local\Programs\Python\Python37
