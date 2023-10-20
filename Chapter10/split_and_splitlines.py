from pathlib import Path

path = Path('Chapter10\\text_files\\try.txt')

contents = path.read_text().split()

print(contents)