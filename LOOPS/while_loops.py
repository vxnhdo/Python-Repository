# While Loops = Execute some code WHILE some condtion is True

# Example 1
name = input("Enter your name: ")
while name == "":
    print("No name entered.")
    name = input("Enter your name: ")

print(f"Hello, {name}. Nice to meet you!")

# Example 2
age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be less than zero.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

# Example 3
food = input("Enter your favorite food (q to quit): ")
while not food == 'q':
    print(f"You like {food}.")
    food = input("Enter your favorite food (q to quit): ")

print("Goodbye!")

# Example 4
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    print(f"{number} is not valid.")
    number = int(input("Enter a number between 1 and 10: "))

print(f"The number entered is {number}.")


