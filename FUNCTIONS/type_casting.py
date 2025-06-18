# Type cast = Process of converting a value of one data type to another
# 4 Python Data Types = (String, Integer, Float, Boolean)

# Explicit Type Casting
name = "Vinh"
age = 21
gpa = 2.5
is_student = True

print(f"Name is a {type(name)}.")
print(f"Age is a {type(age)}.")
print(f"GPA is a {type(gpa)}.")
print(f"Is student is a {type(is_student)}.")


# Explicit Type Conversion
age = float(age) # integer to float
print(age) # 21.0

gpa = int(gpa) # float to integer
print(gpa) # 2

is_student = str(is_student) # boolean to string
print(is_student) # True

age = bool(age) # integer to boolean
print(age) # True

name = bool(name) # string to boolean
print(name) # True

# Implicit Type Conversion
# - when a data type is converted automatically
x = 2
y = 2.0
x = x / y
print(x) # 1.0