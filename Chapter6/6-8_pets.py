pets = []

pet = {
    'owner': 'hadi',
    'kind': 'cat',
    'name': 'lasso',
}
pets.append(pet)

pet = {
    'owner': 'ary',
    'kind': 'bird',
    'name': 'dodo',
}
pets.append(pet)

pet = {
    'owner': 'syarifah',
    'kind': 'fish',
    'name': 'dorry',
}
pets.append(pet)

for pet in pets:
    print(f"here what i know about {pet['name']}")
    for key, value in pet.items():
        print(f"\t{key}: {value}")