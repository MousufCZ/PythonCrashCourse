"""Modifying a List in a Function"""
print("####################################################")
print("###### - unlimited number of arguments in parameter")
print("####################################################\n")

def make_pizza(
        size,
        *toppings):
    
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
