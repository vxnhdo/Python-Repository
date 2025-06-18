# Logical Operators = Evaluate multiple conditions (and, or, not)
# OR = At least 1 condition must be true
# AND = Both conditions must be true
# NOT = Inverts the condtion (Not False = True, Not True = False)

temp = 95
is_raining = False
is_hot = True

if temp > 85 or temp < 0 or is_hot:
    print("Event is cancelled.") # Event is cancelled.

else:
    print("Event is on schedule to occur.")

if temp >= 80 and is_hot:
    print("It will be hot today.") # It will be hot today.
elif temp <= 0 and is_hot:
    print("It will be warm today.")
elif 85 > temp > 0 and is_hot:
    print("It is hot and sunny outside.")
elif temp >= 85 and not is_hot:
    print("It is hot but not sunny outside.")
else:
    print("It is not hot or sunny today.")