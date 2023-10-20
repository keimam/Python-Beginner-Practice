from pathlib import Path
import json



def greet_user(path):
    
    username = get_stored_username(path)
    if username:
        print(f"Welcome Back {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

def get_stored_username(path):
    """Get Stored username"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):

    username = input("What is your name ? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"we will remember when you back {username}")
    return username

def check_user(user):
    """Check the username"""
    path = Path('Chapter10\\text_files\\username.json')
    read_user = path.read_text()
    check = json.loads(read_user)

    if user == check:
        greet_user(path)
    elif user != check:
        get_new_username(path)



user = input("what is your username: ")
check_user(user)