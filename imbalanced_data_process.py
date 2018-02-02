#-*- coding:utf-8-*-
import imblearn
from imblearn.over_sampling import SMOTE
import pandas as pd
from pandas import DataFrame
import numpy as np
import copy

old_data=pd.read_csv('D:\pydata\mypydata\lottery\\wave_value_result_nozero_2.csv',encoding='utf-8')
data1=DataFrame(old_data)
list1=data1.columns
list2=[]
for x in list1:
    if x not in ['event_type','instance']:
        list2.append(x)
X=np.array(data1.loc[:,list2])
for i in X:
    print(np.isnan(i))
# y=np.array(data1['event_type'])
# x_res,y_res=SMOTE(random_state=30,k_neighbors=3).fit_sample(X,y)
# print(len(x_res))
