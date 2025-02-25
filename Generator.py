# Generator
def Gen_fun():
  yield 2
  yield 3
  yield 4 
gen = Gen_fun()
print(next(gen))
print(next(gen))
print(next(gen))
