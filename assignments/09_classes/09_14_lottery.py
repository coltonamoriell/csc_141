from random import sample

# Create a list containing a series of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Randomly select 4 unique items from the pool
winning_ticket = sample(lottery_pool, 4)

# Print the winning message
print("Any ticket matching these 4 numbers or letters wins a prize:")
print(winning_ticket)