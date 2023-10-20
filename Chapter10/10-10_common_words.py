from pathlib import Path

def count_common_words(filename, word):

    path = Path(f"Chapter10\\text_files\\{filename}")

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("The file not found")
    else:
        word_count = contents.lower().count(word)
        print(f"{word} appear in {filename} count {word_count} times")

filename = 'alice.txt'
count_common_words(filename, 'the')