# Functions = A block of reusable code; Place a () after the function name to invoke it

# - position of parameters & arguments MATTER

# Name Function
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
    print()

full_name = create_name("Greg", "Craft")
print(f"Your full name is {full_name}.") # Your full name is Greg Craft.

# Leap Year Example
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Invalid Month."
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2025)) # False
print(days_in_month(2025, 5)) # 31

courses = ["Math", "Art"]
information = {"name": "Vinh",
               "age": 22}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info(*courses, **information)



def hello_func():
    print("Hello function.")

    # or

def hello_function():
    return "Hello function."

print(hello_func()) # Hello function.

# Print a function 3 times
# for x in range(3):
   # print(hello_func())


def happy_birthday(name, age):
    print(f"Happy Birthday {name}, you are {age} years old.")
    print()

happy_birthday("Greg", 21) # Happy Birthday Greg, you are 21 years old.

def display_invoice(user, amount, due_date):
    print(f"Hello {user}, your bill of ${amount}, is due on {due_date}.")
    print()

display_invoice("vxnhdo", 1000, "06/01/2026")

# Return statement = Used to end a function & send back a result to caller

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(add(5, 5)) # 10
print(subtract(15, 7)) # 8
print(multiply(6, 6)) # 36
print(divide(49, 7)) # 7.0






