# TASK: Create a login system that checks if a username & password are correct. Then checks if the user is banned or has admin privileges

correct_user = "admin"
correct_pass = "123"
banned_user = "hacker"

username = input("Enter username: ")
password = input("Enter password: ")

if username == banned_user:
    print("Access denied.")
elif username == correct_user and password == correct_pass:
    print("Login successful!")
elif username != correct_user and password != correct_pass:
    print("Invalid credentials.")
else:
    print("Something went wrong, error.")