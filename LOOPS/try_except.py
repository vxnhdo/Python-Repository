# Use Try-Except for Division Calculator with error handling 
# 1. Ask the user for 2 numbers
# 2. Divide the 1st number by the 2nd number
# 3. Use a try-except loop to catch invalid input (non-numeric or divide by 0)

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        product = num1 / num2

        print(f"Result = {num1} / {num2} = {product:.2f}")
        print()
        break

    except ValueError: # Built-in exception class
        print("Please enter valid numbers.")
        print()
    except ZeroDivisionError: 
        print("Cannot divide by zero.")
        print()

    # 1. ValueError = When a function receives am argument of the correct type but an inappropriate value
    # 2. ZeroDivisionError = When you try to divide a number by zero