import pandas as pd
#count(),sum(),product()
jd=pd.read_csv('C:/Users/abhis/OneDrive/Desktop/python/batsman_runs_ipl.csv')

print(jd.sum())

#basically pandas provide multiple mathematical functions they are
#count,sum,product,mean,mode,std,var,min,max,describe
#describe -- provide summary of following dataset

print(jd.describe())