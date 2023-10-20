dream_vacations_poll = {}

poll_active = True

while poll_active:
    name = input("What is your name? ")
    dream_vac = input("Where is your dream vacation? ")

    dream_vacations_poll[name] = dream_vac

    repeat = input("do you like to respond another person? (yes/no)")

    if repeat == 'no':
        poll_active = False

for name, dream_vac in dream_vacations_poll.items():
    print(f"{name} want to go to {dream_vac} someday")