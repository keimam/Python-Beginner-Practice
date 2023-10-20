from pathlib import Path
import json

path = Path('Chapter10\\text_files\\users.json')


users = {}

if path.exists():
    contents = path.read_text()
    user = json.loads(contents)

    for key, value in user.items():
        print(f"Username : {key} \nPassword : {value}")
else:
    while True:
        name = input("Username: ")
        if name == 'q':
            break

        password = input("Password: ")
        if password == 'q':
            break

        users[name] = password
        content = users

        contents = json.dumps(content)
        path.write_text(contents)