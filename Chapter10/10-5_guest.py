from pathlib import Path

path = Path('Chapter10\\text_files\\guest.txt')

name = input("What is your name ?: ")

contents = f"Hi {name} you are the guest"

path.write_text(contents)