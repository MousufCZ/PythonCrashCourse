"""Return a dictionary of information about a person."""
print("#################################")
print("###### - Function with While Loop")
print("#################################\n")


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\n Please tell me your name: ")
    first = input("First name: ")
    last = input("Last name: ")

    formatted_name = get_formatted_name(first, last)
    print("\nHello, " + formatted_name + "!")
    
