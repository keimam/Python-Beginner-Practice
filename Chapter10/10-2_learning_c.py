from pathlib import Path

path = Path('Chapter10\\text_files\\learning_python.txt')

contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('can', 'could')
    print(line)