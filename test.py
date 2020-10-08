import h5py  # 导入工具包
import pandas as pd
import numpy
from numpy import ndarray
from pandas import DataFrame
import gc
from tqdm import tqdm

import h5py
import gc
import numpy as np
#HDF5的写入：

#HDF5的读取：
f = h5py.File('data/totalExposureLog.h5','r') #打开h5文件
# 可以查看所有的主键
index = 0

name = np.ndarray([])
data = np.ndarray([])
for key in f.keys():
    for index,i in enumerate(f[key].keys()):

        if index == 0:
            # name = np.ndarray([bytes('aid_request','utf-8')])
            continue

        if index == 1:
            data= f[key][i].value.reshape(102386695,1)
            # print(data,2)
            continue
        if index % 2 != 0:
            # print(f[key][i].value)
            data = np.concatenate((data, f[key][i].value), axis=1)
            # print(data.shape)
            print('****************')

        # else:
        #     print(f[key][i].value)
        #     name = np.concatenate((name, f[key][i].value), axis=0)
        #     print(name)


    gc.collect()
    # print(f[key],f[key]['block2_items'].name)
# print(data.size)
# row = data[0][0]
# print(row)
print(data.shape, data.size)
data = np.delete(data, [0], axis=1)

print(data.shape, data.size)
