# Format Specifiers = {value:flags}, format a value based on what flags are inserted

p1 = 3.14159
p2 = 999.999999
p3 = 12.9999
p4 = 123456

print(f"Price 1 = {p1:.2f}") # 3.14
print(f"Price 2 = {p2:.10}") # Allocates 10 spaces 
print(f"Price 3 = {p3:010}") # 00012.9999, zero padded 

print(f"Price 1 is {p1:<10}") # Left Justify
print(f"Price 2 is {p2:>10}") # Right Justify
print(f"Price 3 is {p3:^10}") # Center Justify

print(f"Price 4 is equal to {p4:,}") # Comma as thousands seperator; 123,456

print(f"Price 4 is also equal to {p4:,.3f}") # 123,456.000; Thousands seperator AND decimal precision 
