from pathlib import Path
import json


path = Path('Chapter10\\text_files\\favorite_numbers.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(number)
else:
    number = input("What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("The number has been write.")


