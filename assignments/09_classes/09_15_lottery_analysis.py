from random import choice

# Define the pool of possibilities (10 numbers and 5 letters)
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Define your specific lottery ticket
my_ticket = [7, 'b', 3, 'e']

def get_random_ticket(possibilities):
    """Generate a random 4-item ticket from the pool without duplicates."""
    ticket = []
    while len(ticket) < 4:
        item = choice(possibilities)
        if item not in ticket:
            ticket.append(item)
    return ticket

plays = 0
winning_ticket = []

# Keep pulling random tickets until the drawn ticket matches your ticket 
# (using set() so order doesn't restrict the match)
while set(winning_ticket) != set(my_ticket):
    winning_ticket = get_random_ticket(possibilities)
    plays += 1

print(f"It took {plays} tries to finally hit the winning combination!")
print(f"Your ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")