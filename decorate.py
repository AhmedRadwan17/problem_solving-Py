def MyFec(func):
  def InsideFunc():
    print("Hello")
    func()
    print("Welcome")
  return  InsideFunc

@MyFec
def Say_Hello():
  print("Ahmed")
Say_Hello()
