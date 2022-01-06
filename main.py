import numpy as np
import pandas as pd
import seaborn as sns
import csv

data=pd.read_csv('D:\program\python\cars\cars_excel.csv')
pd.set_option('display.max_columns',27)
print(data.describe())
print(type(data))
print(data['symboling'].head())
print(data.dtypes)
print(data.head(2))
print(data.shape)
print(data[['width','height','length']].head())
print(data.describe(include='object'))
print(data['make'].value_counts()[0:4])
print(len(data.columns))
print(data.head())
print(data.loc[data['make']=='audi',:])
print(data.loc[data['price']>data['price'].mean() ,:])
print(data['price'].mean())
print(data.info())
print(data['engine-size']==data['engine-size'].astype(float))
data['area']=data['width']*data['height']
print(data.head(1))
print(data.head(2))
print(data[['length','width','height']].describe())
data['length_nor']=data['length']/data['length'].max()
print(data['length_nor'])
data['width_nor']=data['width']/data['width'].max()
print(data['length_nor'])
data['height_nor']=data['length']/data['height'].max()
print(data['height_nor'])
print(data.head(1))
print(data['make'].value_counts()/data['make'].count()*100)
data['make'].replace({'toyota':'toto'},inplace=True)
print(data['make'].value_counts())
print(data['make'].str.upper())
print(data.groupby('make')['price'].mean().sort_values(ascending=False))
print(data.columns)
print(data.groupby(['num-of-doors','drive-wheels'])['price'].mean().head(3))
print(data.columns)
cat=data[[x for x in data.columns if data[x].dtype=='object']]
print(cat)

print([y for y in data['price']if y > data['price'].mean()])
a,b=np.histogram(data['price'],3)
print(a)
print(b)
price_cat=pd.cut(data['price'],b,labels=['low','med','high'])
print(price_cat)
data['price_cat']=price_cat
print(data.head(3))
print(data['price_cat'])

