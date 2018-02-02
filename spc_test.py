from pyspc import *
import numpy as np
fake_data=np.random.randn(20,6) + 200
list1=[10,9,12,14,8,6,7,9,10,11,8,9,12,11,10]
np1=np.array(list1)
a= spc(fake_data) + xbar_rbar() + rbar() + rules()
print(a)

