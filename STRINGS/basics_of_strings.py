message = "Hello World"
print(message)      # prints variable 'message'
print(len(message)) # 11 elements

multi_string = """Gregcraft was found in...
WalMart."""
print(multi_string) # prints the multi-line string using triple quotes

print(message[0]) # H; accessing index number
print(message[0:5]) # Hello
print(message[6:])  # World

# String Methods 
print(message.lower()) # hello world
print(message.upper()) # HELLO WORLD
print(message.count("Hello")) # 1; finds at 1st index
print(message.count("l")) # 3; finds 3 l's
print(message.find("World")) # 6; at 6th index
print(message.replace("World", "Universe")) # Hello Universe

new_message = message.replace("World", "Gregs")
print(new_message) # Hello Gregs


greeting = "Hello"
name = "Bob"

# String Concatenation
awesome_message = greeting + ", " + name + ". Welcome!"
print(awesome_message) # Hello, Bob. Welcome!

great_message = f"{greeting}, {name.upper()}. You have arrived!"
print(great_message) # Hello, BOB. You have arrived!
