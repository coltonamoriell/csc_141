'''

chapter 4 assignment 12


'''



# Start with the original list of foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# Make a copy of the list using a slice
friend_foods = my_foods[:]

# Add a new food to each list to keep them distinct
my_foods.append('cannoli')
friend_foods.append('ice cream')

# Print my favorite foods using a for loop
print("My favorite foods are:")
for food in my_foods:
    print(food)

# Print my friend's favorite foods using a for loop
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)