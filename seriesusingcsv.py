import pandas as pd
df = pd.read_csv(
    'C:/Users/abhis/OneDrive/Desktop/python/batsman_runs_ipl.csv',
    index_col='batter'
).squeeze(True)
print(df)
#-----------------------------------------------------------------------#
#series methonds
#head(),tail()
w=df.head(2)#no.of top values to print
print(w)
x=df.tail()
print(x)

#sample -randomly select any random datain csv

s=df.sample(2)#we can ad vbalues so random n values will be selected
print(s)

#values_count
v=df.value_counts()
print(v)

#sort_values

sort=df.sort_values().head(1)#asending=false prints decending should be add in value of values()
print(sort)

#to change to oiginal data in soting order

df.sort_values(inplace=True)


#sort_index this just sort data based on index whether its numeric or char

df.sort_index()# inplace is applcible accordling 