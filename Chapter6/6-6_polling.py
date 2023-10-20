favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name} use {language}.")
print("\n")
coders = ['adam', 'gio', 'senja', 'dikta', 'afif', 'sarah', 'phill']

for coder in coders:
    if coder in favorite_languages.keys():
        print(f"{coder.title()} thanks for respondend")
    else:
        print(f"hi {coder.title()} would you like to poll")