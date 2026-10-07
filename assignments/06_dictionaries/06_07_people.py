'''
Colton Amoriell
i under stand it 8/10
chapter 6 assignment 7



'''
# Exercise 6-1: Original person dictionary
person_1 = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
}

# Exercise 6-7: Creating two new dictionaries for different people
person_2 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': 76,
    'city': 'princeton',
}

person_3 = {
    'first_name': 'marie',
    'last_name': 'curie',
    'age': 67,
    'city': 'paris',
}

# Storing all three dictionaries in a list called people
people = [person_1, person_2, person_3]

# Looping through the list and printing everything known about each person
for person in people:
    # Format the full name cleanly
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"\nInformation about {full_name}:")
    
    # Print the rest of the details
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")