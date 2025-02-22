friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
def Mark(text):
    return text[-1] == "m"
    
myresults=filter(Mark,friends_filter)
print(list(myresults))

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

myresults=filter(lambda text:text[-1] == "m" ,friends_filter)
print(list(myresults))
