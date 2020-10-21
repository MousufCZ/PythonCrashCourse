req_topping = ['mushroom', 'extra cheese']

if req_topping != 'anchovies':
    print("Hold the ancho\n\n")

if 'mushroom' in req_topping:
    print("Ypur pizza has mushroom.")

if 'pepper' in req_topping:
    print("Your pizza has pepper.")
else:
    req_topping.append('pepper')
    print("Adding pepper to your pizza.")

print("\nFInished making your pizza, it has the following toppings: ")
print(req_topping)
