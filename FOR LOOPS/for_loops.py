# For Loop = Execute a block of code a fixed number of items
# - used to iterate over a range, string or sequence
for x in range(1, 11):
    print(x)
 
for x in reversed(range(1, 11)): # Print in reversed order
    print(x)

for x in range(1, 11, 2): # Adds a step to the print
    print(x)

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue # skips 13
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        continue # stops at 13
    else:
        print(x)

successful = True
for x in range(3):
    print("Attempt", x + 1)
    if successful:
        print("Successful.")
        break
    else:
        print("Unsuccessful.")


for x in range(5): # Outer Loop prints 0-4 
    for y in range(3): # Inner Loop prints 0-2
        print(f"{x}, {y}")

print(type[5]) 
print(type(range(5))) # <class 'range'>

for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x) # 1 2 3 4 

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(f"Even number: {x}")
