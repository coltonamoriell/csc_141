'''

chapter 4 assignment 11

'''


# Start with your original list of pizzas
pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Make a copy of the list using a slice
friend_pizzas = pizzas[:]

# Add a new pizza to your original list
pizzas.append('margherita')

# Add a different pizza to your friend's list
friend_pizzas.append('bbq chicken')

# Print your favorite pizzas using a for loop
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Print your friend's favorite pizzas using a for loop
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)