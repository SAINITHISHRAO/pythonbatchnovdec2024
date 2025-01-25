x=5
print(f"x before operation: {x}")
x = x / 0  # This will cause an error

import pdb
x = 5
pdb.set_trace()  # Debugger starts here
x = x / 0


def divide(a, b):
    return a / b

x = 10
y = 0
print(f"x: {x}, y: {y}") 
result = divide(x, y)