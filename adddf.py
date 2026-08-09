import pandas as pd
import matplotlib as plt
movies=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/movies.csv')
movies['country']='India'#creating new columns
print(movies.head())
movies.dropna(inplace=True)
lead_actor=(movies['actors'].str.split('|').apply(lambda x:x[0]))#creating new column for exixting column
print(lead_actor)
#important dataframe functions
ipl=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/ipl-matches.csv')
ipl['ID']=ipl['ID'].astype('int32')
print(ipl.info())