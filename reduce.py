from functools import reduce

# الطريقة الأولى: باستخدام دالة عادية
def Sum(num1, num2):
    return num1 + num2

x = [1, 2, 3, 4, 5, 10, 22]

# تطبيق reduce باستخدام الدالة العادية
result1 = reduce(Sum, x)
print("المجموع باستخدام دالة عادية:", result1)

print("-" * 40)  # فاصل بين الطريقتين

# الطريقة الثانية: باستخدام تعبير lambda
result2 = reduce(lambda num1, num2: num1 + num2, x)
print("المجموع باستخدام تعبير lambda:", result2)
