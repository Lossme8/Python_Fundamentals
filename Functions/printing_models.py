# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complete_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    complete_models.append(current_design)

    # Display all completed models.
print("\nThe following models have been printed:")
for complete_model in complete_models:
    print(complete_model)
print("\n\n---------------------------------------")


# Use functions to make the above code more efficient.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    move each design to complete_models fter printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("\nPrinting model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """ Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', ' robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
