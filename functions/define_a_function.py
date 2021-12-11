# use the keyword 'def', then the name and the parameters if any

def print_bananas(amount):
    'prints banana amount times' # this is a docstring
    print("banana " * amount)

# How to see the function documentation
# print(print_bananas.__doc__)

# invoke the function
how_many = int(input("How many bananas? "))

print_bananas(how_many)
