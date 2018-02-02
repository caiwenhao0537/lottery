#-*- coding:utf-8 -*-
import pandas as pd
from math import isnan
import numpy
from pandas import DataFrame
data1=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_result.csv',encoding='utf-8',header=0,index_col='wave_time')
dataframe1=DataFrame(data1)
list1=list(dataframe1.columns)
list2=['wave_time','instance']
list3=[item for item in list1 if item not in list2]
#print('wave_time' in(list3))
for i in list3:
    sum_num=0
    #print(isnan(sum_num))
    for j in dataframe1[i]:
        if isnan(j):
            j=0
        sum_num=sum_num + float(j)
    if sum_num==0.0:
        dataframe1.drop([i],axis=1,inplace=True)
dataframe1.to_csv('D:\pydata\mypydata\lottery\wave_value_result_nozero.csv',encoding='utf-8')
