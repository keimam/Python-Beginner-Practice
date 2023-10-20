people = []

person = {
    'name': 'hadi',
    'live': 'tengah tani',
    'age': 25
}
people.append(person)

person = {
    'name': 'indra',
    'live': 'harmoni',
    'age': 30,
}
people.append(person)

person = {
    'name': 'hari',
    'live': 'mundu',
    'age': 28
}
people.append(person)

for people_info in people:
    name = f"{people_info['name'].title()}"
    location = f"{people_info['live'].title()}"

    print(f"{name} live in {location}")