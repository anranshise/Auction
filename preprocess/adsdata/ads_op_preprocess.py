#%%
import pandas as pd
import numpy as np

#%%
path = '../../data/'

# 广告操作数据
ad_operation = pd.read_table(path + 'ad_operation.dat',
                             names=['aid', 'update_time', 'op_type', 'op_field',
                                    'modify_field'])
ad_operation = pd.DataFrame(ad_operation)
print(len(ad_operation))

# %%
ad_operation.loc[(ad_operation['update_time']!=0)&(ad_operation['aid']==571403)]


# %%
# ad_operation.loc[()]
ad_operation.loc[(ad_operation['update_time']!=0)&(ad_operation['op_type']==2)]

#%%
ad_operation['update_time'] = ad_operation['update_time'] + 28800
ad_operation['update_time'] = pd.to_datetime(
						ad_operation['update_time'])
ad_operation['update_time_day'] = ad_operation['update_time'].apply(
    lambda x: x.strftime('%Y%m%d'))

ad_operation['day_of_week'] = ad_operation['update_time'].apply(
	 lambda x: x.dayofweek)
ad_operation['hour'] = ad_operation['update_time'].apply(
	 lambda x: x.hour)

print(ad_operation[:3])
# %%
print(ad_operation.loc[(ad_operation['aid']==457009)])

# %%
print(ad_operation.loc[(ad_operation['aid']==457009)])

# %%
