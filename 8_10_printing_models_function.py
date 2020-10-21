"""Modifying a List in a Function"""
print("###############################################")
print("###### - Modifying & not - a List in a Function")
print("###############################################\n")


def print_models(unprinted_designs, completed_models):
    
    """ Simulate printing each design, until none are left.
        Move each design to completed_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        """ Simulate creating a 3D print from the design. """
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Display all completed models. """
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iPhone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) # [:] Keeps the original list intact
show_completed_models(completed_models)
print(unprinted_designs)