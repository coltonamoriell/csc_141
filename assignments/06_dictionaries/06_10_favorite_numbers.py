'''

Colton Amoriell
i under stand it 8/10
chapter 6 assignment 10


'''
favorite_numbers = {
    'mandy': [42, 17],
    'micah': [23, 5, 8],
    'gus': [7, 14],
    'hank': [1_000_000, 42],
    'maggie': [0, 9, 100],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")