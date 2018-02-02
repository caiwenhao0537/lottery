#-*- coding:utf-8 -*-
import pandas as pd
from pandas import DataFrame
old_data=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_result.csv',encoding='utf-8')
unuseful_data=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_result.csv',encoding='utf-8')
old_data_dataframe=DataFrame(old_data)
unuseful_data_dataframe=DataFrame(unuseful_data)
list1=list(old_data_dataframe.columns)
list2=list(unuseful_data_dataframe.columns)
list3=[item for item in list1 if item not in list2]
new_data_dataframe=DataFrame(old_data_dataframe[list3])
new_data_dataframe.to_csv('D:\pydata\mypydata\lottery\wave_value_result_nozero.csv',encoding='utf-8')
