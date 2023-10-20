from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        #Count the approximate number of words in the file
        words = contents.split()
        num_word = len(words)
        print(f"file {path} has about {num_word} words.")

files = ['try.txt', 'heisdi.txt', 'learning_python.txt']

for file in files:
    path = Path(f'Chapter10\\text_files\\{file}')
    count_words(path)