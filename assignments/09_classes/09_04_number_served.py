class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and customer count."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of 0

    def describe_restaurant(self):
        """Print the restaurant's information."""
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It serves delicious {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Add the given amount to the number of customers served."""
        self.number_served += additional_customers


# Create an instance called restaurant
restaurant = Restaurant('The Golden Spoon', 'Italian')

# 1. Print the initial number of customers served (default 0)
print(f"Initial customers served: {restaurant.number_served}")

# 2. Change this value directly and print it again
restaurant.number_served = 15
print(f"Customers served (after direct change): {restaurant.number_served}")

# 3. Call set_number_served() with a new number and print the value again
restaurant.set_number_served(50)
print(f"Customers served (after set_number_served): {restaurant.number_served}")

# 4. Call increment_number_served() to simulate a busy day of business
restaurant.increment_number_served(125)
print(f"Customers served (after incrementing for a day's business): {restaurant.number_served}")