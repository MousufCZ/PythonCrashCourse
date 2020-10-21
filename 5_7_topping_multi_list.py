toppings = ['mushrooms', 'olives', 'green peppers',
            'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested in requested_toppings:
    if requested in toppings:
        print("Adding " + requested + ".")
    else:
        print("Sorry, we don't have " + requested + ".")

print("++++++++++++++")
print("We have finished making your pizza")

    
