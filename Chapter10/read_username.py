from pathlib import Path
import json

path = Path('Chapter10\\text_files\\username.json')

contents = path.read_text()
username = json.loads(contents)

print(username)