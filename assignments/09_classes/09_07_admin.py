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


class Admin(User):
    """Represent an administrator profile with special privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can edit site settings"
        ]

    def show_privileges(self):
        """Display the administrator's set of privileges."""
        print(f"\nPrivileges for Administrator '{self.username}':")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an instance of Admin
admin_user = Admin('Sarah', 'Connor', 'admin_sarah', 'sarah.c@example.com', 'Los Angeles')

# Call the inherited method and the new privilege-displaying method
admin_user.describe_user()
admin_user.show_privileges()