#-*-coding:utf-8-*-
import re
import pandas as pd
from pandas import DataFrame
data=pd.read_csv('D:\pydata\mypydata\lottery\wave_value_result_nozero.csv')
df=DataFrame(data)
old_title=list(df.columns)

list1=[]
for i in old_title:
    i=re.sub('\d','',i)
    i=re.sub('\(','',i)
    i=re.sub('\)','',i)
    list1.append(i)
new_df=DataFrame(list1).T
new_df.to_csv('D:\pydata\mypydata\lottery\\new_title.csv')
