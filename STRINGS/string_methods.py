text = "hello"
print(text.capitalize()) # UPDATED: Hello

t1 = "MARIo"
print(t1.casefold()) # UPDATED: mario; casefold() - processed text into a version that can be compared w/o worrying about other case

t2 = "Luigi"
print(t2.center(20)) # .center() - sets the amount of space to center the string


t3 = "abc_abc_abc_abc"
print(t3.count("abc")) # 4; counts the # of times of occurences

t4 = "Elon Musk"
print(t4.encode(encoding="UTF-8", errors="strict")) # b'Elon Musk'

t5 = "apple"
print(t5.endswith("e")) # True; endswith() - checks if string ends with a character

t6 = "text\ttext2\ttext3"
print(t6.expandtabs(20)) # text                text2               text3

t7 = "Comment and Subscribe."
print(t7.find("Subscribe")) # 12; find() - where target begins

t8 = "{subject} is doing {action}"
print(t8.format(subject="Cat", action="running")) # Cat is doing running

coordinates = {"x": 10, "y": -5}
t9 = "Coordinates: ({x}, {y})"
print(t9.format_map(coordinates)) # Coordinates: (10, -5)

t10 = "Astronauts discovered Diet Coke on the Moon."
position = t10.index("Diet Coke")
print(position) # 22
print(t10[position:]) # Diet Coke on the Moon.

t11 = "hellokitty123"
print(t11.isalnum()) # True