#slicig of multi-dimen arrays

import numpy as np

var=np.array([9,8,7,6,5])

print(var[2])
print(var[-4])

#mult-dim
var2=np.array([[1,2,3],[5,6,7]])

print(var2)
print(var2.ndim)

print(var2[0,2])

var1=np.array([[[1,2],[1,2]]])
print(var1)
print(var1.ndim)
print(var1[0,1,1])

#slicing 