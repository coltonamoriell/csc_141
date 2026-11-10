class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the restaurant's information."""
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It serves delicious {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip', 'Cookies and Cream']

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"\nAvailable flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Create an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand('Sweet Scoops')

# Call the inherited method and the new flavor-displaying method
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()