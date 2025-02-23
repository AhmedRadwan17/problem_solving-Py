import random
print("Random Numbers between 10 and 50 is:",random.randint(10,50))
print("Random Even Numbers between 2 and 10 is:",random.randrange(2,11,2))
print("Random Odd Numbers between 1 and 9 is:",random.randrange(1,10,2))
print("-"*40)
for x in dir(random):
  print(f"-  {x}  -")
