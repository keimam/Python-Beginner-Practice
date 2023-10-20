responses = {}
# Set a flag to indicate that pollings is active.

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("What is your name? ")
    response = input("which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    repeat = input("would you like to let another person respond? (yes/no)")

    if repeat == 'no':
        polling_active = False

print('\n--- Polls Result ---')
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
    