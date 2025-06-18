lang = "Python"
if lang == "Python": 
    print("Language = Python") # Language = Python
elif lang == "Java":
    print("Language = JavaScript")
elif lang == "C++":
    print("Language = C++")
else:
    print("No Match,")

user = "Admin"
logged_in = True
if user == "Admin" and logged_in:
    print("Admin Access") # Admin Access
else:
     print("Partial Access")

a = [1, 2, 3]
b = [4, 5, 6]
print(a == b) # False
print(a is b) # False

c = [7, 8, 9]
d = c
print(c is d) # True
print(id(c) == id(d)) # True

condition = False
if condition:
    print("Evaluation is true.")
else:
    print("Evaluation is false.")

number = 20
if number:
    print("Number is true.") # Number is true; since number > 0
else:
    print("Number is fake.")

name = "Greg"
if name:
    print(f"Your name is {name}")
else:
    print("No name detected.")