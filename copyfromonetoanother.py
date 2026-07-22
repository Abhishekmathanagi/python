with open("first.txt","r") as f1,open("example.txt","w") as f2:
    for line in f1:
        f2.write(line)
        
print("file copied sucessfully")