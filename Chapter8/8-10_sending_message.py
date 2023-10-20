# def show_messages(message):
#     """Show List Text Messages"""
#     for message in message:
#         print(f"- {message}")

def send_message(message, sent_message):
    """Print each text message and move to sent message""" 
    while message:
        msg = message.pop()
        print(f"This is the message would be sent {msg}")
        sent_message.append(msg)

def completed_sent_message(sent_message):
    print(f"\nmessage succsed")
    for message in sent_message:
        print(f"-{message}")

text_messages = ['hello', 'how are you', 'are you happy?']
sent_message = []

send_message(text_messages, sent_message)
completed_sent_message(sent_message)