from pathlib import Path

path = Path("Chapter10\\text_files\\pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthdan, in the form mmddyy: ")
if birthday in pi_string:
    print("Your Birthday appears in the first million digit of pi")
else:
    print("Your birthday doesnt appear in the first million digits of pi")
    