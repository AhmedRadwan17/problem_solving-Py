my_friends = []

maxNumberInList = 4

while 0 < maxNumberInList:
    userInput=str(input("enter Your Name: "))
    if(userInput.isupper()):
        print("Invaild Name ")
        break
    else:
        maxNumberInList-=1
        print(f"Friend {userInput} has Added Successfully!\nNames Left in list {maxNumberInList}")
        my_friends.append(userInput)
        
if len(my_friends)!=0:
    print(my_friends)