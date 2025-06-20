# Using For-loops, ask user for a number then print the multiplication table. Allow the user to enter the number & choose how far the table should go (20 to 50 etc).

num = int(input("Enter the number for the multiplication table: "))
max_limit = int(input("Enter the range for the multiplication table: "))
print(f"\nMultiplication Table for {num}: 1 to {max_limit}:\n")
for i in range(1, max_limit + 1): # For each number from 1 up to AND including max_limit
    result = num * i # result equals num times i
    print(f"{num} X {i} = {result}.")