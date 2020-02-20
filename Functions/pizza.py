# passing an Abitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese', 'feta')
print("\n-----------------end of function call-----------")


def make_pizza2(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza2('cherry tomato', 'goat cheese', 'olives')
make_pizza2('bacon', 'ground beef', 'chicken', 'herbs')
print("\n-----------------end of function call-----------")


# Mixing Positional and Arbitrary Arguments.
def make_pizza3(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza3(16, 'herbs')
make_pizza3(12, 'bacon', 'ground beef', 'extra cheese')
