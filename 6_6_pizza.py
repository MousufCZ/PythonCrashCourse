#pizza.py
# Store information about a pizza being ordered.
# List in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summerize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)
