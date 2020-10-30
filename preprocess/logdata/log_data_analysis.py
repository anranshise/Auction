#%%
import h5py  # 导入工具包
import pandas as pd
from numpy import ndarray
from pandas import DataFrame
import gc
from tqdm import tqdm
import numpy as np

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
log_data = log_data.groupby(['aid'])\
.agg({'uid': 'count'}).reset_index().rename(columns={'uid': '曝光数'})

print(log_data[:2])
print(len(log_data))

#%%
log_data = log_data.groupby(['hour'])\
.agg({'request_id': 'count'}).reset_index().rename(columns={'request_id': '曝光数'})
#%%
log_data
#%%

plt.plot(log_data['hour'],log_data['曝光数'] )
plt.show() 
# %%
log_data = log_data.groupby(['aid'])\
.agg({'request_id': 'count'}).reset_index().rename(columns={'request_id': '曝光数'})
plt.plot(log_data['aid'],log_data['曝光数'])
plt.show() 
# %%
# %%
log_data = log_data.groupby(['request_time_day'])\
.agg({'request_id': 'count'}).reset_index().rename(columns={'request_id': '曝光数'})

# %%
plt.plot(log_data['request_time_day'],log_data['曝光数'])
plt.show() 
# %%
len(log_data)
# %%
log_data[40:100]
# %%

# %%
log_data = log_data.groupby(['request_id'])\
.agg({'aid': 'count'}).reset_index().rename(columns={'aid': '曝光数'})

# %%
plt.plot(log_data['request_id'],log_data['曝光数'])
plt.show() 
# %%
log_data.loc[(log_data['location_id'] == 168) & (log_data['request_time_day']=='20190218')]



#选取满足某个类别的条件。 C 是产品类型。 选c =3或5，6的所有样本

# %%
log_data = log_data.groupby(['uid', 'request_time_day'])\
.agg({'location_id': 'count'})

# %%
