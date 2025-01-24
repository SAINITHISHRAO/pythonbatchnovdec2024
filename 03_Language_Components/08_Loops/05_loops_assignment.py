# Assignment: Try these break, continue, pass, on a for loop example
for i in range(1,10):
    if i == 5:
        print("Using pass for", i)
        pass  # Placeholder
    elif i % 2 == 0:
        print("Using continue for", i)
        continue  # Skip the even numbers
    elif i == 9:
        print("Using break for", i)
        break  # Exit the loop
    print("i =", i)