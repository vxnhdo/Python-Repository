weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds? (K/L): ")
if unit == "K" or unit == "k":
    weight *= 2.205
    print(f"Your weight in pounds is: {weight:.2f} lbs.")
elif unit=="L" or unit=="l":
    weight /= 2.205
    print(f"Your weight in kilograms in: {weight:.2f} kgs.")
else:
    print(f"{unit} is NOT allowed.")