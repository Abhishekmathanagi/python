lines=0
word=0
char=0

with open("first.txt","r") as f:
    for line in f:
        lines+=1
        word+=len(line.split())
        char=len(line)
        
print(line)
print(word)
print(char)