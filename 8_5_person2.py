"""Return a dictionary of information about a person."""
print("##############################")
print("###### - Returning Dictionary")
print("##############################\n")

def build_person(first_n, last_n, age= ''):
    person = {'first': first_n,
              'last': last_n}
    if age:
        person['age'] = age
    return person

musician = build_person('mousuf','zaman', age= 27)
print(musician)
