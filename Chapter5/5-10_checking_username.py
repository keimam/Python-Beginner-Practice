usernames = ['miki', 'lisa', 'nana', 
             'admin', 'tia']
lower_usernames = [user.lower() for user in usernames]

new_username = ['tio', 'rama', 'Tia']

for username in new_username:
    if username.lower() in lower_usernames:
        print(f"username {username} already Exist")
    else:
        print(f"Hi {username}")
    

# if usernames:
#     for username in usernames:
#         if 'admin' in username:
#             print(f"Hi {username}. want to see report")
#         else:
#             print(f"Hello {username} thanks for login in")
# else:
#     print('we nedd to find some user')