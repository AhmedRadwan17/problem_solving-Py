# zip()
list1 = [1,2,3,4,5]
list2 = ["A","B","C"]
dict1 = {"Name":"Ahmed","Age":22}
y = zip(list1,list2)
for x in y :
    print(x)
for item1 , item2 , item3 in zip(list1,list2,dict1):
    print(f"list 1 item: {item1}")
    print(f"list 2 item: {item2}")
    print(f"list 3 Key : {item3} and value : {dict1[item3]}")
