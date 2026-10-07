'''

Colton Amoriell
i under stand it 8/10
chapter 6 assignment 6


'''
# The base dictionary from favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List of people who should take the poll (some are in the dictionary, some are not)
people_to_poll = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

# Loop through the list to check their status
for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"Hi {person.title()}, please take a moment to vote for your favorite language!")