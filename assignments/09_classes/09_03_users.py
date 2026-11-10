class User:
    """A simple model to represent a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize core user attributes and profile details."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's profile information."""
        print(f"\nUser Profile: {self.username}")
        print(f"  Full Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back. Glad to have you here.")


# Create several instances representing different users
user1 = User('Alice', 'Smith', 'asmith99', 'alice.smith@example.com', 'New York')
user2 = User('Marcus', 'Johnson', 'mjohnson_dev', 'marcus.j@example.com', 'Seattle')
user3 = User('Elena', 'Rodriguez', 'elena_r', 'elena.rodriguez@example.com', 'Austin')

# Store users in a list to easily loop through them and call both methods
users = [user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()