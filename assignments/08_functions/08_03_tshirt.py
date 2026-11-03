def make_shirt(size, message):
    """Summarize the size and message of the t-shirt."""
    print(f"Making a size {size} t-shirt with the message: '{message}' printed on it.")


# 1. Calling the function using positional arguments
make_shirt('medium', 'Python is Fun!')

# 2. Calling the function using keyword arguments
make_shirt(size='large', message='Code, Sleep, Repeat.')