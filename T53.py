import numpy as np
import matplotlib.pyplot as plt

courses=['C++','Python','高数','大学英语','软件工程','组成原理','数字图像处理','计算机图形学']
score=[80,95,78,85,45,65,80,60]
courses=np.append(courses,courses[0])
dl=len(score)
angles=np.linspace(0,
                   2*np.pi,
                   dl,
                   endpoint=False)
score.append(score[0])
angles=np.append(angles,angles[0])
plt.polar(angles,score,'rv--',linewidth=2)
plt.thetagrids(angles*180/np.pi,courses,fontproperties='simhei')
plt.fill(angles,score,facecolor='r',alpha=0.6)
plt.show()