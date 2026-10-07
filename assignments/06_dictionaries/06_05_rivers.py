'''

Colton Amoriell
i under stand it 8/10
Chapter 6 assignment 5


'''
# 1. Create a dictionary containing three major rivers and their countries
rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon': 'brazil'
}

# 2. Loop to print a sentence about each river
print("--- River Descriptions ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n--- River Names ---")
# 3. Loop to print the name of each river included in the dictionary
for river in rivers.keys():
    print(river.title())

print("\n--- Country Names ---")
# 4. Loop to print the name of each country included in the dictionary
for country in rivers.values():
    print(country.title())