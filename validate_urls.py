import re

readmore = 'y'
list1 = []

while readmore.lower() == 'y':
    
    My_String = input("Enter your URL: ")
    Check = re.findall(r'(https?://)(www\.)?(\w+(\.\w+)+)', My_String)

    if Check:
        print("Valid URL!,",end=" ")
    else:
        print("Invalid URL!")

    if Check:
        list1.append(My_String)
        print("Added Successfully!")
        readmore = input("Do you want to add emails: ")
    else:
        print("Not Valid")
        readmore = 'n'
counter=1     
if readmore.lower() != 'y':
    print("End Add,",end=" ")
    if list1:
        print("Emails in Database are:")
        for email in list1:
            print(f"({counter}) {email}")
            counter +=1
