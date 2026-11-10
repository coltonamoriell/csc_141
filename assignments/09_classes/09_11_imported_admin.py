"""A set of classes used to represent users, privileges, and administrators."""

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


class Privileges:
    """A separate class to store and display administrator privileges."""

    def __init__(self, privileges=None):
        """Initialize the privileges attribute with a default list."""
        if privileges is None:
            self.privileges = [
                "can add post", 
                "can delete post", 
                "can ban user", 
                "can edit site settings"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Display the administrator's set of privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an administrator profile using composition for privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """
        Initialize attributes of the parent class.
        Then initialize a Privileges instance as an attribute.
        """
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()