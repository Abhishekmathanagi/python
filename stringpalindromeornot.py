name=input().replace(" ","").lower()
print(type(name))
print(name)

if name==name[::-1]:
    print("true")
else:
    print("false")
