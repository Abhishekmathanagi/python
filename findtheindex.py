new=(1,23,141,42,124,31)
try:
    print(new.index(23))
except ValueError:
    print("element not found")