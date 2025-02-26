# Errors 
x=input("enter number?")
print(type(x))
if type(x) == int or str :
    raise Exception ("Error")
    raise ValueError("Error")
else:
    print("True")
