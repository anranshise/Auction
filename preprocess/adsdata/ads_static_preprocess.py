#%%
import pandas as pd
import numpy as np

#%%
path = '../../data/'

# 广告静态数据
ad_static_feature = pd.read_table(path + 'ad_static_feature.out',
                                  names=['aid', 'create_time', 'account_id', 'goods_id',
                                         'goods_type', 'industry_id', 'aid_size'])
# %%
ad_static_feature = pd.DataFrame(ad_static_feature)
len(ad_static_feature)
# %%
ad_static_feature.loc[(ad_static_feature['create_time']==0)]

# %%
ad_static_feature['create_time'] = ad_static_feature['create_time'] + 28800
ad_static_feature['create_time'] = pd.to_datetime(
						ad_static_feature['create_time'], unit='s')
ad_static_feature['create_time_day'] = ad_static_feature['create_time'].apply(
    lambda x: x.strftime('%Y%m%d'))

# %%
print(ad_static_feature['create_time_day']=='20190218'[:10])

# %%
print(ad_static_feature.loc[(ad_static_feature['aid']==457009)])
# %%
