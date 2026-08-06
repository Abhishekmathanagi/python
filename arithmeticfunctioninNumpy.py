#np.min(),np.max(),np.argmin(),np.sqrt(),
# np.sin(),np.cos(),np.cumsum()
import numpy as np

var=np.array([1,2,3,4,5,6])
print(np.min(var))
print(np.max(var))
print(np.argmin(var),np.argmax(var))

var1=np.array([[1,2,3,4],[6,7,8,9]])
print(np.min(var1,axis=0),np.min(var1,axis=1))
print(np.sqrt(var1))

ar1=np.array([1,2,3,4,5])
print(np.sin(ar1))
print(np.cos(ar1))
print(np.cumsum(ar1)) #kinda palindrome