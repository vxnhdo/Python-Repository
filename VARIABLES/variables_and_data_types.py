# Variable = Reusable container for storing a value, behaves as if it were the value it contains

age = 21
print(age) # 21
print("You are " + str(age) + " years old.") # You are 21 years old.
print("You are ", age, " years old.") # OR
print(f"You are {age} years old.") # OR

# Integers = Whole numbers ONLY!
players = 30
quantity = 30
print(f"There are {players} basketball players on the team.")
print(f"I have a pack of {quantity} Diet Coke.")

# Floats = Decimal numbers
gpa = 3.0
distance = 26.2
price = 79.99
print(f"Your gpa is: {gpa}.")
print(f"There are {distance} miles in a marathon.")
print(f"That T-Shirt costs {price}.")

# Strings = Text
name = "Greg"
food = "Cheeseburgers"
pet = "Cat"
print(f"Your name is {name} and you like {food}.")
print(f"I have a pet {pet}.")

# Booleans = True or False
online = True
on_sale = True
running = True
print(f"Online Status: {online}.") # Online Status: True.
print(f"Sale status: {on_sale}.") # Sale status: True.
print(f"Is the Website running?: {running}.") # Is the Website running?: True.

if online:
    print("There is internet access.") # There is internet access.
else:
    print("You are offline.")