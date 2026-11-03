def make_shirt(size='large', message='I love Python'):
    """Summarize the size and message of the t-shirt."""
    print(f"Making a size {size} t-shirt with the message: '{message}' printed on it.")


# 1. Large shirt with the default message
make_shirt()

# 2. Medium shirt with the default message
make_shirt(size='medium')

# 3. Shirt of any size (small) with a different message
make_shirt(size='small', message='Keep Calm and Code On')