import re
mystring = "I Love Python"
mysearce=re.split(" ",mystring)
print(mysearce)
print(re.sub("-"," ","I-Love-Python"))
