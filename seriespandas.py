import pandas as pd
import numpy as np

marks=[56,65,76,87,90]
subjects=['telugu','hindi','english','maths','science']

o=pd.Series(marks)
print(o)

#custom series
#additionally we can add name to corresponding series
p=pd.Series(marks,index=subjects,name='abhishek marks')

print(p)

