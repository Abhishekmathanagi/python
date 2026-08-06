import numpy as np

x=np.array([1,2,3,4,5,6,7,8])

for i in x:
    print(i)
    
    
var=np.array([[1,2,3,4],[9,7,6,5]])

for j in var:
    print(j)
    
    
#to handle multi-dime we can use nditer() in for loopp

var2=np.array([[[1,2,3,4],[1,2,4,6]]])
for k in np.nditer(var2):
    print(k)
    
#to print all the ndexes and data in mult-dime 
#we can use ndenumerate()


var3=np.array([[[1,2,3,4],[1,2,4,6]]])
for x,d in np.ndenumerate(var2):
    print(x,d)