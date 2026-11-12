def send_messages(messages, sent_messages):
    """Print each text message and move it to sent_messages."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: '{current_message}'")
        sent_messages.append(current_message)

# 1. Start with a list of short text messages and an empty sent list
text_messages = [
    "Hey, are we still meeting up later?",
    "Don't forget to pick up groceries on your way home.",
    "Python functions are actually pretty cool!",
    "Call me when you get a chance."
]
sent_messages = []

# 2. Call the function using a copy of text_messages [:]
send_messages(text_messages[:], sent_messages)
