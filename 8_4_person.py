"""Return a dictionary of information about a person."""
print("##############################")
print("###### - Returning Dictionary")
print("##############################\n")

def build_person(first_n, last_n):
    person = {'first': first_n,
              'last': last_n}
    return person

musician = build_person('mousuf','zaman')
print(musician)
