'''

Colton Amoriell
i under stand it 8/10
chapter 6 assignment 9


'''
# Create the favorite_places dictionary with names as keys and lists of places as values
favorite_places = {
    'sarah': ['grand canyon', 'kyoto', 'paris'],
    'alex': ['yosemite', 'tokyo'],
    'marissa': ['reykjavik', 'maui', 'banff']
}

# Loop through the dictionary using the .items() method
for name, places in favorite_places.items():
    # Print the person's name, capitalized cleanly
    print(f"\n{name.title()}'s favorite places are:")
    
    # Loop through the list of places for the current person
    for place in places:
        # Print each place indented with a bullet point
        print(f"  - {place.title()}")
