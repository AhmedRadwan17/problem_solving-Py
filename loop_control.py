Numbers =[1,3,4,5,6,8,9,9,8,10,11,12]

for number in Numbers:
    if number == 10:
        break
    
    print(number)

print("-"*40)
for number in Numbers:
    if number == 10:
        continue 
    
    print(number)