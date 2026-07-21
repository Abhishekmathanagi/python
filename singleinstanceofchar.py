from collections import Counter
s1=input()
cout=Counter(s1)

for char in cout:
    if cout[char]==1:
        print(char)
        