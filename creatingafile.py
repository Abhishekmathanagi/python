with open("first.txt","w") as f:
    f.write("my name is abhishek\n")
    f.write("this a file handlings\n")
    
import os
print("File saved at:", os.path.join(os.getcwd(), "example.txt"))