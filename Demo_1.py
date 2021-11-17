import numpy as np
from numpy import matlib as mt

a=np.array([[1,1,1],[2,2,2],[3,3,3]])
b=np.array([10,20,30])

print(a)
print(b)
print(a*b)

# print(mt.empty((3,3),dtype=int))
# print(mt.ones((3,3)))
# print(mt.eye(n=3,M=3,k=0,dtype=int))
#
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.mat(a)
# c=np.mat('123,456,789')
# print('创建矩阵b:\n',b)
# print('创建矩阵c:\n',c)
# print('矩阵b类型:',type(b),'矩阵c类型',type(c))
# print('矩阵b转换为数组：',type(np.asarray(b)))
# print('矩阵a转换为数组：',type(np.asmatrix(a)))

# a=np.arange(1,10)
# b=np.array([[1,3,5],[2,4,6,],[8,10,12]])
#
# print(a)
# print(b)
#
# #求数组中的最大值
# print(np.max(a))
# print(np.max(b))
# print(np.amax(b))
# print(np.amax(b,axis=1))#求纵向序列的最大值
# print(np.amax(b,axis=0))#求横向序列的最大值
# print(np.ptp(a))#求元素差，最大-最小
# print(np.ptp(b))
# print(np.ptp(b,axis=0))
# print(np.ptp(b,axis=1))
# print(np.sum(a))
# print(np.sum(b))#求和
# print(b)
# print(np.sum(b,axis=0))#竖向
# print(np.sum(b,axis=1))#横向
#
# print(np.sum(np.arange(1,101,1)))



# a=np.random.uniform(range(1,6),6)
# b=np.random.uniform(range(1,6),6)
# print(a)
# print(b)
# print(np.add(a,b))#加
# # np.subtract()#减
# # np.divide()#乘
#
# print(np.mod(a,b))#除法
# print(np.mod(np.fix(a),np.fix(b)))#除法取余


# a=np.random.uniform(range(1,6),6)
# print(a)
# print(np.round(a))
# print(np.round(a,decimals=1))#保留小数点后一位
# print(np.round(a,decimals=2))#后两位
# print(np.round(a,decimals=-1))#四为0五10并取整
# print(np.rint(a))#四舍五入并取整
# print(np.floor(a))#比几点几小
# print(np.ceil(a))#比几点几大
# print(np.fix(a))#取整


# a=np.array([0,30,45,60,90])
# print(np.sin(a))
# print(np.sin(a*np.pi/180))
# print(np.cos(a*np.pi/180))
# print(np.tan(a*np.pi/180))
#
# arcsin=np.arcsin(np.sin(a*np.pi/180))#反正弦
# print(arcsin)
#
# print(np.degrees(arcsin))
#
# print(np.radians(a))#角度对应的弧度
# print(np.rad2deg(np.radians(a)))#弧度对应的角度


# a=np.arange(9).reshape(3,3)
# print(a)
# b=np.hsplit(a,3)#纵向
# print(b)
# c=np.vsplit(a,3)#横向
# print(c)
#
# d=np.split(a,3,axis=0)#默认o
# print(d)
#
# e=np.split(a,3,axis=1)
# print(e)
#
# aa=np.arange(9)
# print(aa)
# f=np.split(aa,[2,4,6])
# print(f)





#Day01
# a=np.array([1,2,3,4,5])
#
# #五个属性
# print(a)
# print(a.dtype)
# print(a.shape)
# print(a.ndim)
# print(a.size)
#
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b)
# print(b.dtype)
# print(b.shape)
# print(b.ndim)
# print(b.size)

# a=np.zeros(4,dtype=int)
# print(a)
# print(a.dtype)
#
# b=np.zeros((3,3),dtype=int)
# print(b)
#
# c=np.ones((5,5))
# print(c)
#
# d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(d)
# print("="*100)
# print(d[1])
# print(d[1:])
# print(d[0,1:])#第0列中，索引为1及之后所有的
#
# print(d[...,1])#2 5 8,前一个参数代表着列，后一个参数代表索引为几
# print(d[1,...])#4 5 6，.为0，..为0 1 ，...为0 1 2
# print(d[...,1:])
#
# e=np.arange(9)
# print(e)
# #变成3行3列的二维数组
# print(e.reshape(3,3))
# print(e.ravel())#变回
# f=e.reshape(3,3)
# print(f.ravel(order='F'))#按列展开
#
# a=np.array([[1,2],[3,4]])
# print(a)
# b=np.array([[5,6],[7,8]])
# print(b)
# d=np.array([[0,9],[9,0]])

# c=np.hstack((a,b))#横向与横向联合两个数组
# print(c)
# d=np.vstack((a,b))#纵向与纵向联合两个数组
# print(d)

# c=np.concatenate((a,b))#直接纵向拼接
# print(c)
# c=np.concatenate((a,b),axis=1)#直接横向向拼接
# print(c)
#
# c=np.concatenate((a,b,d),axis=1)
# print(c)
