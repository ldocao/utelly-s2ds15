###PURPOSE: plot pairwise plot of all numerical variables

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




csvfile = "../io/phoenix.event.csv"

df = pd.read_csv(csvfile)
colnames = df.columns.values
#df.columns = np.arange(0,df.columns.size).tolist() ##rename columns with indices


##plot only numerical and boolean
is_numerical = np.array(df.dtypes == np.float64)
is_boolean = np.array(df.dtypes == np.bool_)
numerical_df = df.loc[:,is_numerical]
boolean_df = df.loc[:,is_boolean]
both_df = pd.concat([boolean_df,numerical_df])
both_df = both_df.replace(to_replace=True,value=1)
both_df = both_df.replace(to_replace=False,value=0)




##plot only numerical
dpi=150
figsize=(64, 48)
plt.figure(figsize=figsize, dpi=dpi)
axes = pd.tools.plotting.scatter_matrix(numerical_df, alpha=0.02,figsize=figsize)
plt.tight_layout()
plt.savefig("pairwise_scatter_numerical.png",dpi=dpi)

##plot only boolean
##this is a stupid plot
plt.figure(figsize=figsize, dpi=dpi)
axes = pd.tools.plotting.scatter_matrix(boolean_df, alpha=0.1,figsize=figsize)
plt.tight_layout()
plt.savefig("pairwise_scatter_boolean.png",dpi=dpi)

##plot both
figsize=(128, 96)
plt.figure(figsize=figsize, dpi=dpi)
axes = pd.tools.plotting.scatter_matrix(both_df, alpha=0.1,figsize=figsize)
plt.tight_layout()
plt.savefig("pairwise_scatter_both.png",dpi=dpi)
