




# List of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'club', 'roast beef', 'pastrami', 'blt']
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami
print("Sorry everyone, the deli has run out of pastrami!\n")

# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the remaining orders, make them, and move them to finished_sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)