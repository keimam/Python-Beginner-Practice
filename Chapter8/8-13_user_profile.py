def build_profile(first, last, **options):
    """Build user profile"""
    user_info = {
        'first_name': first.title(),
        'last_name': last.title(),
    }
    for option, value in options.items():
        user_info[option] = value
    
    return user_info

user_info = build_profile('imam', 'nasehudin', age=23, status='active')
print(user_info)