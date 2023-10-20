from pathlib import Path

path = Path('Chapter10\\text_files\\learning_python.txt')

contents = path.read_text()

for line in contents.splitlines():
    line = line.replace('can', 'could')
    print(line)