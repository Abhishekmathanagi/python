import pandas as pd
#indexing ,sclicing,fancy indexing ,labeling with sclicing 

np=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/movies.csv',index_col='title_x')

print(np.iloc[3])
print(np.iloc[1:6])
print(np.iloc[1,2])