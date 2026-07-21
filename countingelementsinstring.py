s=input()
vowels="aeiouAEIOU"
vowelcount=0
consocount=0
numcount=0
specialcount=0

for char in s:
    if char.isalpha():
        if char in vowels:
            vowelcount+=1
        elif char not in vowels:
            consocount+=1
    elif char.isdigit():
        numcount+=1
    else:
        specialcount+=1

print(vowelcount)
print(consocount)
print(numcount)
print(specialcount)