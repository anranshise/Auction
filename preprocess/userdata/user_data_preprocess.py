#%%
import pandas as pd
import numpy as np

#%%
path = './data/'

# 用户数据
user_feature = pd.read_table(path + 'user_data', sep='\t',
                             names=['uid', 'age', 'gender', 'area', 'status',
                                    'education', 'consuptionAbility', 'device',
                                    'work', 'connectionType', 'behavior'])
# %%
user_feature = pd.DataFrame(user_feature)
print(user_feature[:3])
# %%
