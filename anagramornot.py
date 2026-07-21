#Check whether two strings are anagrams.
s1=input()
s2=input()
sort1=sorted(s1)
sort2=sorted(s2)
sortchar1="".join(sort1)
sortchar2="".join(sort2)

if sortchar1==sortchar2:
    print("the string is a anagram")
else:
    
    print("its not a anagram")