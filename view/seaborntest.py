import numpy as np
import pandas as pd
from scipy import stats,integrate
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import seaborn as sns
sns.set(color_codes=True)

#random种子值设置
np.random.seed(sum(map(ord,"distributions")))
#正太分布数组
x = np.random.normal(size=100)
#柱状图hist
#plt.hist(x)

#连续的变量rug
#sns.kdeplot(x,shade=True)

#hist+rug
#sns.distplot(x)
#sns.distplot(x,hist=False,rug=True)

# x = np.random.gamma(6,size=200)
# sns.distplot(x,kde=False,fit=stats.gamma)

mean,cov = [0,1],[(1,.5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)
df = pd.DataFrame(data,columns=["x","y"])

#plt.scatter(df['x'].values,df['y'].values)
# sns.jointplot(x="x",y="y",data=df)
# sns.jointplot(x="x",y="y",data=df,kind='hex')
# sns.jointplot(x="x",y="y",data=df,kind='kde')
f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)
plt.show()
