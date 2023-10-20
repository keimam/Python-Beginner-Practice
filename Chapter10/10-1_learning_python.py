from pathlib import Path

path = Path('Chapter10\\text_files\\learning_python.txt')

lines = path.read_text()
print(lines)

print("\n--------------")

lines = lines.splitlines()

for line in lines:
    print(line)