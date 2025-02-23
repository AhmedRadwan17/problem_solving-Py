skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
counter=enumerate(skills)
for index , value in counter:
    if type(value) ==str:
        print("(",index,"-",value,")")
        
