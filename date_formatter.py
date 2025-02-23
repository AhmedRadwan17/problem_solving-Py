# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10 "

import datetime
TheDateBefore = datetime.datetime(2021,6,25)

TheDateAfter = datetime.datetime(2021,8,10)

print(f"Days From: \n{TheDateBefore} To {TheDateAfter} are: {(TheDateAfter-TheDateBefore).days} Days")
print("-"*40)

# Today Is "2021, 8, 10"
Date_Time =  datetime.datetime(2021,8,10)
print(Date_Time)
print("(",end="")
print(Date_Time.strftime("%Y"),end="-")
print(Date_Time.strftime(f"{Date_Time.month} %B"),end="-")
print(Date_Time.strftime(f"{Date_Time.day} %A"),end="")
print(")")
