'''

Colton Amoriell
i under stand it 8/10   
Chapter 6 assignment 8


'''
# Create individual dictionaries for each pet
pet_1 = {
    'name': 'Rex',
    'kind': 'dog',
    'owner': 'Alice',
}

pet_2 = {
    'name': 'Whiskers',
    'kind': 'cat',
    'owner': 'Bob',
}

pet_3 = {
    'name': 'Bubbles',
    'kind': 'goldfish',
    'owner': 'Charlie',
}

# Store the dictionaries in a list called pets
pets = [pet_1, pet_2, pet_3]

# Loop through the list and print everything known about each pet
for pet in pets:
    print(f"\nHere is what I know about {pet['name']}:")
    print(f"\tKind of animal: {pet['kind']}")
    print(f"\tOwner's name: {pet['owner']}")