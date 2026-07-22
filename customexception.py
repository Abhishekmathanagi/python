    
class AgeTooLowError(Exception):
    """Raised when age is below 18"""
    pass

def registration(age):
    if age < 18:
        raise AgeTooLowError("Must be 18 or older")
    else:
        print("Registration is successful")
        
try:
    n = int(input())
    registration(n)
except AgeTooLowError as e:
    print("Age is low:", e)
