import pandas as pd
import matplotlib as plt
df=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/movies.csv',index_col='title_x')

plot=df.plot()
print(plot)