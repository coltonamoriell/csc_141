"""A class representing a user profile."""

class User:
    """A model to represent a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize core user attributes and profile details."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's profile information."""
        print(f"\nUser Profile: {self.username}")
        print(f"  Full Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back. Glad to have you here.")



