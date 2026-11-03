def make_sandwich(*items):
    """Summarize the sandwich being ordered with the given items."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with a different number of arguments
make_sandwich('turkey', 'swiss cheese', 'lettuce', 'mayo')
make_sandwich('ham', 'cheddar')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey', 'toasted bread')