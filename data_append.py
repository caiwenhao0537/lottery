#-*- coding:utf-8 -*-
import pandas as pd
from pandas import DataFrame
import numpy
#读取数据
frame_wave_value1=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_1.csv',encoding='utf-8',header=0,index_col='wave_time')
frame_wave_value2=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_1_11_15.csv',encoding='utf-8',header=0,index_col='wave_time')
frame_wave_value3=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_2.csv',encoding='utf-8',header=0,index_col='wave_time')
frame_wave_value4=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_2_11_15.csv',encoding='utf-8',header=0,index_col='wave_time')
#frame合并
frame_dataframe_value1=DataFrame(frame_wave_value1)
frame_dataframe_value2=DataFrame(frame_wave_value2)
frame_dataframe_value3=DataFrame(frame_wave_value3)
frame_dataframe_value4=DataFrame(frame_wave_value4)
#输出处理结果
frame_dataframe_value1.append(frame_dataframe_value2).append(frame_dataframe_value3).append(frame_dataframe_value4).to_csv('D:\pydata\mypydata\lottery\wave_value_result.csv',encoding='utf-8')


