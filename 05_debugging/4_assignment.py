#Assignment: How to clear one specific breakpoint, in ipdb
import ipdb

def some_function():
    x = 5
    y = 10
    ipdb.set_trace()
    result = x + y
    print(f"The result is: {result}")

if __name__ == "__main__":
    some_function()

