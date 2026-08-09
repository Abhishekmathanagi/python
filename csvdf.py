import pandas as pd
import numpy as np

data=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/movies.csv')
ipl=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/ipl-matches.csv')

#dataframes attributes and methods
print(data.shape)
print(data.dtypes)
print(data.index)
print(data.columns)
print(data.values)
print(data.head(5))#to retrive top 5 values
print(data.tail(5))#to retrive last 5 values
print(data.sample(5))#which provide random values 
print(data.info())#provide details of data 
print(data.describe())#provides summary of corresponding data
print(data.isnull().sum())
print(data.duplicated())
#mean,median,std,var with axis argument