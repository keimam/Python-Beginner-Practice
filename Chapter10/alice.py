from pathlib import Path

path = Path('Chapter10\\text_files\\alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("The file doesn't exist")
else:
    # Count the approximate number of word in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has abuot {num_words} words.")