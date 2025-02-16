friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
a = 0
counter =0
while a < len(friends):
    if not friends[a].islower():
        counter+=1
        print(friends[a])  
    
    a += 1
print(f"Friends Printed and Ignored Names Count Is {len(friends)-counter}")