x = [1, 2, 3, 4, 10, 11]

# استخدام دالة عادية مع filter
def CheckNumber(number):
    return number < 10

MyResults = filter(CheckNumber, x)

print("باستخدام الدالة العادية:")
for number in MyResults:
    print(number)

print("-" * 40)

# استخدام تعبير lambda مع filter
MyResults = filter(lambda num: num < 10, x)

print("باستخدام تعبير lambda:")
for number in MyResults:
    print(number)
