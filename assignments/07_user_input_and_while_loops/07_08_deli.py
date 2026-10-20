




# Create the list of sandwich orders and an empty list for finished sandwiches
sandwich_orders = ['tuna', 'turkey', 'club', 'roast beef', 'blt']
finished_sandwiches = []

# Loop through the orders until the list is empty
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\n--- All sandwiches have been made! ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")