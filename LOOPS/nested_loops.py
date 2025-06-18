# Nested Loops = Loop within another loop (outer, inner)
# - used for working with 2D data such as lists, patterns or combinations

# Repeat 3 times
for x in range(3):
    for y in range(10):
        print(x, end="") # Instead of a newline after x, print nothing
    print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


# Basic structure:
for i in range(3): # 0 1 2
    for j in range(2): # 0 1
        print(i, j)


# TASK #1: Print a multiplication table for numbers 1 to 5
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end= ' ')
    print()


# TASK #2: Print a Right-Angled Triangle of Stars
n = 4
for n in range(1, n):      # Outer Loop = from 1 to n
    for j in range(n):     # Inner Loop = print i stars
        print("*", end='') # Prints star without new line
    print() # Move to the next line after each row 


# TASK #3: For i & j from 1 to 3, print all pairs where i is NOT equal to j
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            print(f"({i}, {j})")
