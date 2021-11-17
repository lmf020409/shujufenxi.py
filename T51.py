import matplotlib as mp
import matplotlib.pyplot as plt

mp.rcParams['font.sans-serif']=['SimHei']
mp.rcParams['axes.unicode_minus']=False

fig=plt.figure()

x=[1,2,3,4,5,6,7,8]
y=[1,3,2,1,6,2,4,6]

left,bottom,width,height=0.1,0.1,0.8,0.8

x1=fig.add_axes([left,bottom,width,height])

x1.plot(x,y,'b')
x1.set_title('子图x1')

left,bottom,width,height=0.2,0.5,0.25,0.25
x2=fig.add_axes([left,bottom,width,height])

x2.plot(x,y,'y')
x2.set_title('子图x2')
plt.show()