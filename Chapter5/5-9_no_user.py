usernames = ['miki', 'lisa', 'nana', 
             'admin', 'tia']

if usernames:
    for username in usernames:
        if 'admin' in username:
            print(f"Hi {username}. want to see report")
        else:
            print(f"Hello {username} thanks for login in")
else:
    print('we nedd to find some user')