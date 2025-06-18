# Indexing = Accessing elements of a sequence using [] (indexing operator)
# [start:stop:step] = slice

# Indexing Example
card = "1234-5678-9012-3456"
print(card[0]) # 1
print(card[1]) # 2
print(card[2]) # 3

print(card[:4]) # 1234; Get first four characters
print(card[5:9]) # 5678; Get second set of four characters
print(card[5:]) # 5678-9012-3456; Get everything after 5th index
print(card[-1]) # 6; Get last index
print(card[::2]) # 13-6891-46; Get every second character
print(card[::-1]) # 6543-2109-8765-4321; Prints in reverse
print(card[-4:]) # 3456; Prints last 4 characters

