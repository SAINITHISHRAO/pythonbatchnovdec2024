# ipdb is a Python debugger that adds an interactive command-line interface for debugging your code. 
# It's like the built-in pdb debugger but with a better interface provided by the IPython library.
# It helps you pause your program, inspect variables, and step through the code to find and fix bugs.

numbers = range(0, 100)

#import ipdb; ipdb.set_trace()

breakpoint()

for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num, end=", ")