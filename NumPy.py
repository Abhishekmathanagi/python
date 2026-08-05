#importing Numpy
import numpy as np;

#creating an arr 
n=np.array([1,2,3,4,5,6,7,8,9,9])
print(n)
print(type(n))

#2darray
arr2=np.array([[1,2,3,4,5,6],[2,4,3,5,4,3]])
print(arr2)
print(arr2.ndim)

#NDIM
arrn=np.array([1,2,3,4,5,6,7],ndmin=10)
print(arrn)
print(arrn.ndim)

#zeros for all 0's
a=np.zeros(5)
print(a)

#ones fucntion to print all 1's
b=np.ones((3,4))
print(b)

#empty function
empty=np.empty((2,2))
print(empty)

#arange function
arr_rang=np.arange(4)
print(arr_rang)

#identity matrix/diagonal
arr_dia=np.eye(5)
print(arr_dia)

#linspace
arr_lin=np.linspace(0,20,num=4)
print(arr_lin)