import numpy as np

var=np.array([1,2,3,4,5,6])

np.random.shuffle(var)
print(var)

uniqe=np.unique(var,return_counts=True)
print(uniqe)

#these are arthematic operations

resize=np.resize(var,(2,3))
print(resize)

