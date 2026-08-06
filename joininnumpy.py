import numpy as np

var1=np.array([1,2,3,4])
var2=np.array([5,6,7,8])

arr=np.concatenate((var1,var2))
print(arr)
#above function can do operations on mult-deme aslo

#stack() aslo used to merge 

var3=np.array([1,2,3,4])
var4=np.array([5,6,7,8])

ar_merge=np.hstack((var3,var4),axis=1)