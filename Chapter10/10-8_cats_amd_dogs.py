from pathlib import Path

files = ['cats.txt', 'dosgs.txt']

for file in files:
    try:
        path = Path(f'Chapter10\\text_files\\{file}')
        contents = path.read_text()
        contents += f"\n"
    except FileNotFoundError:
        print(f"The file name {path} not found")
    else:
        print(contents)