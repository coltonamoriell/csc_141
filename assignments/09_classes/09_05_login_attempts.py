class User:
    """A model to represent a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize core user attributes and profile details, including login attempts."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Default value of 0

    def describe_user(self):
        """Print a summary of the user's profile information."""
        print(f"\nUser Profile: {self.username}")
        print(f"  Full Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back. Glad to have you here.")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0


# Make an instance of the User class
user = User('Alice', 'Smith', 'asmith99', 'alice.smith@example.com', 'New York')

# Call increment_login_attempts() several times (e.g., 3 times)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts to check proper incrementation
print(f"Login attempts after incrementing: {user.login_attempts}")

# Call reset_login_attempts()
user.reset_login_attempts()

# Print login_attempts again to verify it was reset to 0
print(f"Login attempts after resetting: {user.login_attempts}")