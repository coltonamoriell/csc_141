class Restaurant:
    """model a restaurant with OOP."""

    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        """Print the restaurant's information."""
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The price is {self.price_range}.")

    def can_you_take_a_date(self):
        """Print a message indicating that the restaurant is open."""
        if self.price_range > 50:
            print(f"Don't embarrass yourself. It's too expensive")
        else:
            print(f"You can afford {self.restaurant_name}.")


# Create three different instances from the Restaurant class
restaurant_one = Restaurant('The Golden Spoon', 'Italian', 'New York', 60)
restaurant_two = Restaurant('Sakura Bistro', 'Japanese', 'Los Angeles', 40)
restaurant_three = Restaurant('Taco Fiesta', 'Mexican', 'Austin', 25)

# Call describe_restaurant() for each instance
restaurant_one.describe_restaurant()
print()
restaurant_two.describe_restaurant()
print()
restaurant_three.describe_restaurant()