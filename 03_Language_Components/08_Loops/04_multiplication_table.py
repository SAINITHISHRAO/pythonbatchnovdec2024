LIMIT = 10

first = 0
while first < LIMIT:
    first += 1
    print(f"{first  =}")

    second = 0
    while second < LIMIT:
        second += 1

    print('%d * %d = %d' % (first, second, first * second))
    print('{} * {} = {}'.format(first, second, first * second))
     

LIMIT = 10

for first in range(1, LIMIT + 1):  # Iterates from 1 to 10
    print(f"Multiplication Table for {first}:")
    
    # Inner loop for reversing the table from 10 to 1
    for second in range(LIMIT, 0, -1):  # Iterates from 10 to 1
        print(f"{first} * {second} = {first * second}")
    
    print()  # Add a blank line between tables     



LIMIT = 10


for second in range(1, LIMIT + 1):
    
    row = []
    
    # Inner loop for columns (multiplicands)
    for first in range(1, LIMIT + 1):
        # Format the result with leading zeros and proper spacing
        formatted_result = f"{first:02} * {second:02} = {first * second:03}"
        row.append(formatted_result)
    
    # Join the row elements with " | " and print the result
    print(" | ".join(row))