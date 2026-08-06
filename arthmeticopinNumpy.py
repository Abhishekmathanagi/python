import numpy as np

#arithmetic operators

var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varadd=var1+var2

print(varadd)
print(varadd*2)
print(varadd/3)
print(varadd%2)

var12=np.add(var1,var2)
print(var12)

###numpy arithematic operators
#np.add(),np.substract(),np.multiply(),np.divide(),np.mod(),np.power()
#np.reciprocal()


#2d
tw=np.array([[1,2,3,4,5],[6,7,8,9,0]])
var=np.array([[1,2,3,4,5],[6,7,8,9,0]])
add2d=np.add(tw,var)
print(add2d)