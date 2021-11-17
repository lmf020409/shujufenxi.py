#-*- coding: utf-8 -*- 
#对数据进行基本的探索
#返回缺失值个数以及最大最小值

import pandas as pd

#pip install xlrd==1.0.0
datafile= r'TB201812.xls'  #原始数据,第一行为属性标签
resultfile = r'view.xlsx' #数据探索结果表

data = pd.read_excel(datafile) #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data=data[['订单付款时间','买家会员名','买家实际支付金额','数据采集时间']]
view = data.describe(percentiles = [], include = 'all',datetime_is_numeric=True).T #包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
view['null'] = len(data)-view['count'] #describe()函数自动计算非空值数，需要手动计算空值数

view = view[['null', 'max', 'min']]
view.columns = [u'空值数', u'最大值', u'最小值'] #表头重命名
'''这里只选取部分探索结果。
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50%（中位数）、max（最大值）'''

view.to_excel(resultfile) #导出结果
