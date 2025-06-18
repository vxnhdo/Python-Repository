# Set = Unordered, Immutable, Add/ Remove OK. NO Duplicates
# - indexing is NOT allowed
# - sets are UNINDEXED collection

veggies = {"Carrot", "Lettuce", "Cucumber", "Spinach"}

print(len(veggies)) # 4
print("Carrot" in veggies) # True
veggies.add("Kale") 
veggies.remove("Spinach")
veggies.pop() # Removes random element
print(veggies)

# To remove duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums)) # Converting a List to a Set then to a List, auto removes duplicates
print(unique_nums) # [1, 2, 3, 4, 5]


# To Find Common Elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = set(a) & set(b)
print(common) # {3, 4}

# To check for duplicates
def is_unique(list):
    return len(list) == len(set(list))

print(is_unique([1, 2, 3])) # True, no duplicates
print(is_unique([1, 1, 1])) # False, yes duplicates





