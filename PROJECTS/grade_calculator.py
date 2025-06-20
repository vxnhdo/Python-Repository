# 1. Ask the user for their test score then return a corresponding letter grade
while True:
    try: # try to run code inside this block
        score = float(input("Enter your test score: "))

        if 0 <= score <= 100:
            break # Valid score then break
        else:
            print("Enter a valid score between 0 and 100.")
    except ValueError: # if code raises ValueError, run this blok
        print("Enter a number, not text.")

if score > 100 or score < 0:
    print("Invalid score, must be between 0 and 100.")
elif score >= 90:
    print("You scored an A.")
elif score >= 80:
    print("You scored a B.")
elif score >= 70:
    print("You scored a C.")
elif score >= 60:
    print("You scored a D.")
else:
    print("You scored a F.")