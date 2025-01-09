# Purpose: Check even-ness of a given number, in runtime.
# Alogorithm: determining odd/even status using the modulus arithmetic operator

number = 33
print(f"{number             = }")
print(f"{number / 2         = }")
print(f"{number % 2         = }")
print(f"{number % 2 == 0    = }")

if number != 0:
    print(f"{number} is non-zero")

if number:
    print(f"{number} is non-zero")


# Assignment: Generate even numbers between 45 & 137
# loop values between limits, test eveness for each number
# and display, if it is even


for number in range(45, 138):  # The range end is also included, so use 138
    # Check if the number is even
    if number % 2 == 0:
        # Print the even number
        print(number)


for number1 in range(33, 56): 
    if number1 % 2 == 0:
        print(number1)        