#iloc-searches using index positions
#loc-seaarches using index labels
#iloc we can slice the data set or we can do fansy indexing 
# data.iloc[0:3,0:3]
#data.loc[0:3,'title','poster_url']
import pandas as pd
import matplotlib as plt
movies=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/movies.csv')
ipl=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/ipl-matches.csv')
mask=ipl['MatchNumber']=='Final'
new_df=ipl[mask]
print(new_df[['Season','WinningTeam']])

mask2=ipl[ipl['SuperOver']=='Y']
print(mask2)
print(mask2.shape)
mask3=ipl[(ipl['City']=='Kolkata') &(ipl['WinningTeam']=='Chennai Super Kings')].shape
print(mask3)
mask4=ipl(ipl['TossWinner']==ipl['WinningTeam'])
print(mask4)
mask5=movies[(movies['imdb_rating']>8.5) & (movies['imdb_votes']>10000)].shape
print(mask5)
mask6 = movies[(movies['genres'].str.split('|').apply(lambda x: 'Action' in x)) & (movies['imdb_rating'] > 7.5)]
print(mask6)
