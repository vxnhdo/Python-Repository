# Tuples = Ordered, unchangable. Duplicates OK, faster
# - items have a defined order and accessible by INDEXING
# - can hold ANY data type
# - must have a COMMA & 1 item 

# TASK #1: Print the 2nd and last items using indexing
colors = ('red', 'green', 'blue', 'yellow')
print(colors[1])
print(colors[-1]) # Will always return the last element

# TASK #2: Unpack the tuple into variables, name, age & profession, then print them
person = ("Alice", 40, "Engineer")
name, age, profession = person
print(f"{name} is {age} years old and works as a {profession}.") # Alice is 40 years old and works as a Engineer.

# TASK #3: Write a function named min_max that takes a list of numbers & returns a tuple, (min, max) of the list
def min_max(list):
    minimum = min(list)
    maximum = max(list)
    return (minimum, maximum) 

result = min_max([1, 2, 3, 4, 5, 60, 70, 80, 90, 100])
print(result) # (1, 100)

'''
name = person[0]
age = person[1]
profession = person[2]
''' 



my_tuple = (1, 2, 3) # creating a tuple
single_tuple = (4,)  # single suple

print(my_tuple[0])  # 1
print(my_tuple[0:]) # (1, 2, 3)

a, b = (10, 20)
print(a, b) # 10 20 (Tuple unpacking)


proteins = ("Steak", "Chicken", "Soy", "Eggs")
print(len(proteins)) # 4 
print("Steak" in proteins) # True

try:
    print(proteins.index("Steak")) # 0
except ValueError:
    print("Item not found in tuple.")

for x in proteins:
    print(x)

