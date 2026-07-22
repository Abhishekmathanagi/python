try:
    num=int(input())
except ValueError:
    print("enter coorrect value only")
except TypeError:
    print("check the value u entered")
except IndexError:
    print("check ur index")
else:
    print(num)
finally:
    print("program is sucuessfully executed")