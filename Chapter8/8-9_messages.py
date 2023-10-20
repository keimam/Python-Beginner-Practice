def show_messages(message):
    """Show List Text Messages"""
    for message in message:
        print(f"- {message}")

text_messages = ['hello', 'how are you', 'are you happy?']

show_messages(text_messages)