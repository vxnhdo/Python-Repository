# Lists = [], ordered * changable. Duplicates OK

fruits = ["Apple", "Banana", "Cherry", "Mango"]
print(fruits) # ['Apple', 'Banana', 'Cherry', 'Mango']

print(fruits[0])    # Apple
print(fruits[0:3])  # ['Apple', 'Banana', 'Cherry']
print(fruits[::2])  # ['Apple', 'Cherry']
print(fruits[::-1]) # ['Mango', 'Cherry', 'Banana', 'Apple']

for x in fruits: # To iterate through fruits list
    print(x)

print(len(fruits)) # 4 ; Prints length of list
print("Apple" in fruits) # True ; will search & return a value in list
 
fruits.append("Pineapple") # Add value to end of list
print("Pineapple" in fruits) # True

fruits.remove("Cherry")
fruits.insert(3, "Watermelon") # insert(index, value)

fruits.sort()    # Alphabetical sort
fruits.reverse() # Reversed based on order
 
print(fruits.index("Banana")) # 3
print(fruits.count("Banana")) # 1

print(dir(fruits)) # Prints list of Methods for collection type
print(help(fruits)) # Lists the description of each Method







