#list:ordered ,mutable,allow duplicates elements 

mylist=["banana","cherry","apple"]

mylist.append("lemon")
mylist.insert(2,"blueberry")
for i in mylist:
    print(i)
print(len(mylist))
mylist.pop()
print(mylist)