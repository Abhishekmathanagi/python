def dectobinay(n):
    if n==0:return " "
    else:
        return  dectobinay(n//2)+str(n%2)
    
print(dectobinay(13))