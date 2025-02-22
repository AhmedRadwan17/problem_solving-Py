print("-"*40)    
print("\t\t\t-----map-----")
print("-"*40)    

# باستخدام دالة عادية
mylist = ["Ahmed", "  SaMy", "Ramy"]
def Print(Name):
    return Name.strip().capitalize()

print("Using Function:")
for name in map(Print, mylist):
    print(name)

print("-"*40)

# باستخدام Lambda
print("Using Lambda:")
for name in map(lambda name: name.strip().capitalize(), mylist):
    print(name)
