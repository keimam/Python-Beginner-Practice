from pathlib import Path

path = Path('Chapter10\\text_files\\guest_book.txt')

prompt = "Hi input your name. \n"
prompt += "Press 'q' to quit.\n"

guestes = []

while True:
    name = input(prompt)

    if name == 'q':
        break

    guestes.append(name)

guest_name = ''
for guest in guestes:
    guest_name += f"{guest}\n"

path.write_text(guest_name)

