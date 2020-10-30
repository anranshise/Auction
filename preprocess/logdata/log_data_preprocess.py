#%%
import h5py  # 导入工具包
import pandas as pd
from numpy import ndarray
from pandas import DataFrame
import gc
from tqdm import tqdm
import numpy as np

#%%
#HDF5的读取：
f = h5py.File('data/totalExposureLog.h5','r') #打开h5文件
# 可以查看所有的主键
index = 0

name = np.ndarray([])
data = np.ndarray([])
for key in f.keys():
    for index,i in enumerate(f[key].keys()):

        if index == 0:
            continue

        if index == 1:
            data= f[key][i].value.reshape(102386695,1)
            continue
        if index % 2 != 0:
            data = np.concatenate((data, f[key][i].value), axis=1)

    gc.collect()
    # print(f[key],f[key]['block2_items'].name)
# print(data.size)
# row = data[0][0]
# print(row)
print(data.shape, data.size)

data = np.delete(data, [0], axis=1) 
print(data.size)

# %%
print(data[0,:])
# %%
data[:,:]=data[:,[4,5,3,6,7,9,8,0,1,2]]

# %%
print(data[0,:])
#%%

data = pd.DataFrame(data)
data.columns = [
    'request_id',
    'request_time',
    'location_id',
    'uid',
    'aid',
    'ad_size',
    'bid',
    'pctr',
    'quality_ecpm',
    'totalEcpm',   
]
# %%
print(data[0:2])
#%%
data = data.drop_duplicates(
    subset=['request_id', 'location_id'], keep='last')

print(data.size)
# %%
data[:2]
# %%
data['request_time'] = data['request_time'] + 28800
data['request_time'] = pd.to_datetime(
						data['request_time'], unit='s')
data['request_time_day'] = data['request_time'].apply(
    lambda x: x.strftime('%Y%m%d'))
data['day_of_week'] = data['request_time'].apply(
	 lambda x: x.dayofweek)
data['hour'] = data['request_time'].apply(
	 lambda x: x.hour)
data['minute_of_day'] = data['request_time'].apply(
	 lambda x: x.minute + x.hour*60)

# %%
data[:2]
#%%
data.to_hdf('data/log_data.h5', key='df', mode='w')

#%%
log_data = pd.read_hdf('data/log_data.h5', key='df')
log_data[:3]

#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#%%
log_data = log_data.groupby(['aid', 'request_time_day'])\
.agg({'uid': 'count'}).reset_index().rename(columns={'uid': '曝光数'})

#%%
log_data[:2]

log_data = log_data.groupby(['hour'])\
.agg({'request_id': 'count'}).reset_index().rename(columns={'request_id': '曝光数'})
#%%
log_data
#%%

plt.plot(log_data['hour'],log_data['曝光数'] )
plt.show() 
# %%
