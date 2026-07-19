num=int(input())
original=num
rev=0

while num>0: 
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev == original:
    print("is palindrome")
else:
     print("not a palindrome")