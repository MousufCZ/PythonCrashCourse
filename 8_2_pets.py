def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')
#describe_pet(animal_type='cat', pet_name='tootoo')
describe_pet(pet_name='mous')
