from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5]

path = Path('Chapter10\\text_files\\numbers.json')

contents = json.dumps(numbers)
path.write_text(contents)