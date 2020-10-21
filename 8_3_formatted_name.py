def get_formatted_name(first, last, middle = ''):
    """Return a full name, neatly formatted."""
    if middle:
        full = first + " " + middle + " " + last
    else:
        full = first + " " + last
    return full.title()

musician = get_formatted_name('mousuf', 'zaman')
print(musician)


musician = get_formatted_name('mousuf', 'c','zaman')
print(musician)




