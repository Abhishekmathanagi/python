import pandas as pd

marks={
    'math':95,
    'english':90,
    'science':99,
    'social':80
}

marks_series=pd.Series(marks)
print(marks_series)

#series attributtes
print(marks_series.size)#size
print(pd.Series(marks_series).is_unique)#is_unique
print(marks_series.index)#index
print(marks_series.values)#vales
