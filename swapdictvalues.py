dict={"a":1,"b":2,"c":4}
swap={}
for k,v in dict.items():
    swap.setdefault(v,[]).append(k)
    
print(swap)