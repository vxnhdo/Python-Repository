# Conditional Expression = A 1-line shortcut for the if-else statement
# - Print / Assign one or mre values based on a condition
# Syntax: x if condition else y or value_if_true if condition else value_if_false

num = 5
print("Positive" if num > 0 else "Negative") # Positive

result = "EVEN" if num % 2 == 0 else "ODD"
print(result) # ODD 

a = 10
b = 5
max_num = a if a > b else b
min_num = a if a < b else b
print(f"Max Num: {max_num}\nMin Num: {min_num}")

age = 21
status = "Adult" if age >= 18 else "Minor"
print(status)

temperature = 90
weather = "HOT" if temperature >= 76 else "COOL"
print(weather)

user_role = "Admin"
access_level = "Full Access" if user_role == "Admin" else "Partial Access"
print(access_level)

username = input("Enter your username: ") or "Guest"
print(f'You entered: {username}')

count = 1
message = f"{count} item{'s' if count != 1 else ''} in cart."
print(message)

a = 5
b = 15
def max_of_two(a, b):
    return a if a > b else b

max_value = max_of_two(a, b)
print(f"Max Value is: {max_value}")

is_member = True
discount = 0.2 if is_member else 0