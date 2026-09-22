'''
chapter 4 assiment 13


'''



# Store five basic foods in a tuple
buffet_foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')

# Print each food the restaurant offers using a for loop
print("Original menu:")
for food in buffet_foods:
    print(food)

# Try to modify one of the items (Uncommenting this line will cause a TypeError)
# buffet_foods[0] = 'burger'

# The restaurant changes its menu, replacing two items
buffet_foods = ('burgers', 'fries', 'carrot cake', 'cannoli', 'ice cream')

# Print each item on the revised menu using a for loop
print("\nRevised menu:")
for food in buffet_foods:
    print(food)