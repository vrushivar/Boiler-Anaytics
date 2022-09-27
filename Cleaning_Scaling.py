# importing important libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")

# creating dataframe of csv datafile
Ndf=pd.read_csv("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\DBN\datafile.csv")
Cdf.head(2)

#cleaning the data
print(Ndf.isnull().sum())
Cdf=Ndf.drop(Ndf.columns[Ndf.isnull().mean()>0.5],axis=1)
raw=Cdf.drop(Cdf.columns[Cdf.isnull().mean()>0.5])
df=raw.fillna(method='ffill')
df.head(2)
df.isnull().sum()
df.drop(['Timestamp'],axis=1,inplace=True)
df.drop(['Timestamp.1'],axis=1,inplace=True)
df = df[df['EFF_Boiler_ON'] != 0]
df = df[df['EFF_SF_Ratio'] != 0]
df.drop(['EFF_Boiler_ON','EFF_Efficiency'], axis=1, inplace=True)
df.drop(['ts','EFF_Blowdown_TDS_Total','EFF_Fuel_Flow_Total','EFF_Furnace_Pressure','EFF_Radiation_Loss','EFF_Steam_Flow_Total','EFF_FeedWater_ECO_OL','DT_FLOW_PL1_Total','PL1_Temp','CRF2'],axis=1, inplace=True)

#scaling the data
df.corr()
#......visualizing by heatmap
plt.figure(figsize=(10,10))
hm = sns.heatmap(df.corr(), vmax=1, square=True,annot=True, cmap="bone")
plt.show()
#......
from sklearn.preprocessing import StandardScaler
xs = x.copy()
num_cols=xs.columns
for i in num_cols:
    scale = StandardScaler().fit(xs[[i]])
    xs[i] = scale.transform(xs[[i]])
x=xs

