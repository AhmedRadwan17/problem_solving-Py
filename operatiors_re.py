import re

# تعريف النصوص
my_string = "I Love Python"
url = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

# تقسيم النص باستخدام المسافات
split_string = re.split(r"\s+", my_string)
print(split_string)
print("-" * 20)

# استبدال "-" بمسافات
modified_text = re.sub(r"-", " ", "I-Love-Python")
print(modified_text)
print("-" * 20)

# البحث عن أجزاء الرابط باستخدام التعبيرات النمطية
search = re.search(r"(https?)://(www\.)?([\w-]+)\.([\w]+)(:\d+)?(/)?(.+)", url)

# طباعة النتائج
print("Full Match:", search.group(), "\n")  
print("-" * 20)
print("Groups:", search.groups())  
print("-" * 20)
print(f"Protocol: {search.group(1)}")
print(f"Domain: {search.group(2)}")
print(f"Port: {search.group(3)}")
print(f"Path: {search.group(4)}")
