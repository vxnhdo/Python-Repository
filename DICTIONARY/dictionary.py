capitals = {"USA": "Washington D.C.", 
            "India": "New Dehli", 
            "Russia": "Moscow", 
            "China": "Beijing"}

# print(dir(capitals)) Attributes & methods for a dictionary
# print(help(capitals))

# .get(key_value) = get a value from a dictionary
print(capitals.get("USA")) # Washington D.C.
print(capitals.get("India")) # New Dehli

if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital does not exist.")

# .update({key:value}) = update the dictionary
capitals.update({"Germany": "Berlin"})
print(capitals.get("Germany")) # Berlin

# .pop(key) = to remove a key-value pair
capitals.pop("Germany")
print(capitals.get("Germany")) # None

# .popitem() = remove most recent key-value pair
# capitals.popitem()

# .clear()= clear entire dictionary

# .keys() = get all keys in dictionary, no values
keys = capitals.keys()
print(keys)

# To iterate all keys in dictionary
for i in capitals.keys():
    print(i)

# .values() = to get all values in dictionary, no keys
values = capitals.values()
for i in capitals.values():
    print(i)

# items() = to print each key-value pair in a dictionary
names = {"Bob": "Bugs", 
         "Greg": "Craft", 
         "Cheeto": "Cheeseburger"}
items = names.items()
print(items)

for key, value in names.items():
    print(f'{key} : {value}')


