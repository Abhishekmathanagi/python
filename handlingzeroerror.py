try:
    num=int(input())
    div=int(input())
    result=num/div
except ZeroDivisionError:
    print("zero cannot be dividede")
else:
    print(result)
finally:
    print("execution done sucessfully")