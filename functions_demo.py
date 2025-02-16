# Simple Function 
def Fun():
    print("Hello!")
Fun()

print("-"*40)

# Unpacking and Packing 
def Fun2(*People):
    for name in People:
        print(f"Hello {name}")
Fun2("Osama","Ahmed","SmSm","Ramy")

# default Function 
print("-"*40)
def Fun3(Name,Age,Country="Unknown"):
    print(f"{Name}, {Age}, {Country}")
Fun3("Ahmed",19)
print("-"*40)

Skills={
    "html":"50%",
    "C++":"50%"
}

def Fun4(Skills):
    for keys , values in Skills.items():
        print(f"{keys} => {values}")
Fun4(Skills)    


print("-"*40)


def Fun5(**Skills):
    for keys , values in Skills.items():
        print(f"{keys} => {values}")
Fun5(html="50%",Java="60%")