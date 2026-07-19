
def gcd(a,b):
    if b==0:return a 
    else:return gcd(a,a%b)
    
a,b=8,6
print(gcd(a,b))