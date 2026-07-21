dict1={"c":10,"a":22,"d":92,"b":12}

sortbyvalue=sorted(dict1.items(),key=lambda item: item[1])
print(sortbyvalue)

dict2={"c":10,"a":22,"d":92,"b":12}

sortbykey=sorted(dict2.items())
print(sortbykey)