#Colton Amoriell
# Difficulty 6/10



# Dictionary to store user responses (name: destination)
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt the user for their name and dream vacation destination
    name = input("\nWhat is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary
    responses[name] = destination

    # Find out if anyone else is going to take the poll
    repeat = input("\nWould you like to let another person respond? (yes/no) ").lower()
    if repeat == 'no':
        polling_active = False

# Polling is complete. Print the results.
print("\n--- Poll Results ---")
for name, destination in responses.items():
    print(f"{name.title()} would love to visit {destination.title()}.")