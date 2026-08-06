
import numpy as np
var=np.array([[1,2,],[1,2]])
print(var)
print()
#to check the shape
print(var.shape)

var1=np.array([1,2,3,4],ndmin=4)
print(var1)
print(var1.ndim)
print(var1.shape)

#reshape a multi-dim array

var2=np.array([1,2,3,4,5,6])

print(var2)
print(var.ndim)

x=var2.reshape(3,2)
print(x)

one=var2.reshape(-1)
print(one.ndim)