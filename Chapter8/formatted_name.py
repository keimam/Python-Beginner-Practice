def get_formated_name(first_name, last_name, middle_name =''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

first_name = input("first name > ")
middle_name = input("Middle name > ")
last_name = input("input your last name > ")

musician = get_formated_name(first_name, last_name, middle_name)
print(musician) 