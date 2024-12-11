# block code - if, else, elif, for, while, def , class, ...
# if 12 > 3:
# print('12 is greater than 3')
# IndentationError: expected an indented block after 'if' statement on line 11

if 12 > 3:
    print("12 is greater than 3")


if 12 > 34:
    print("greater")
else:
    print("It is lesser")

i = 0
while i < 10:
    print(i)
    i += 1



def my_func():
    return "hello world"


class MyClass:
    def __init__(self):
        pass



# tabs vs white-space
# PEP 8 (Python Enhancement Proposal) - code style guide
# Prefer white-spaces, to tabs; four white-spaces