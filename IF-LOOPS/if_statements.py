# If = Do some code only IF condition is True, else do something else
age = int(input("Enter your age: "))
if age >= 100:
    print("Too old to qualify.")
elif age < 0:
    print("Not born yet.")
elif age >= 18:
    print("You qualify.")
else:
    print("Unqualified.")


response = input("Would you like food? ( y / n ): ")
if response == 'y':
    print("Eat food.")
else:
    print("No food.")


name = input("Enter your name: ")
if name == "":
    print("No name entered.")
else:
    print(f"Hello {name}!")


for_sale = True
if for_sale:
    print("Item is on sale.")
else:
    print("Item is NOT for sale.")