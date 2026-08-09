import pandas as pd
import numpy as np
student=[
    [100,40,23],
    [90,70,7],
    [200,40,54]
]

df=pd.DataFrame(student,columns=['iq','marks','package'])
print(df)
#dict
student_dict={
    'iq':[100,90,120,80],
    'marks':[90,80,50,60],
    'packages':[20,18,29,30]
    
}
print()
dfdict=pd.DataFrame(student_dict)
print(dfdict)
print(student_dict.values)