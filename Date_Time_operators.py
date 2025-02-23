import datetime

for x in dir(datetime):
  print(f"- {x} -")

for y in dir(datetime.datetime):
  print(f"- {y} -")

# Print The Current Date
print(datetime.datetime.now())

# Print The Current Day
print(datetime.datetime.now().day)

# Print The Current Year 
print(datetime.datetime.now().year)

# Print The Current Month 
print(datetime.datetime.now().month)

# Print The Current Hour 
print(datetime.datetime.now().hour)

# Print The Current Time
print(datetime.datetime.now().time())

# Print The Current Hour
print(datetime.datetime.now().time().hour,end=":")

# Print The Current Minute
print(datetime.datetime.now().time().minute,end=":")

# Print The Current Second
print(datetime.datetime.now().time().second)

# Specific Date 
Birthday=datetime.datetime(2006,9,15)
Current_Date=datetime.datetime.now()
print(Current_Date-Birthday)
print((Current_Date-Birthday).days)
