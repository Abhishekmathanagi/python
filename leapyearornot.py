def leapyear(year):
    if year%4==0:
        return "yes"
    else:
        return "not"
    
year=int(input())
print(leapyear(year))