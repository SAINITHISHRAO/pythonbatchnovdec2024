# Hexadecimal to Octal
hex_num = input("Enter a hexadecimal number: ")
# Convert hex to decimal, then to octal
decimal_num = int(hex_num, 16)
octal_num = oct(decimal_num)
print(f"Hexadecimal {hex_num} is Octal {octal_num[2:]}")

# Octal to Hexadecimal
oct_num = input("Enter an octal number: ")
# Convert octal to decimal, then to hex
decimal_num = int(oct_num, 8)
hex_num = hex(decimal_num)
print(f"Octal {oct_num} is Hexadecimal {hex_num[2:].upper()}")
