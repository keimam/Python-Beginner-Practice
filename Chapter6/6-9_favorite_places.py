favorite_places = {
    'hadi': ['kamer', 'pegunungan'],
    'ipeh': ['kamer', 'pantai'],
    'imam': ['pegunungan'],
}

for names, places in favorite_places.items():
    if len(places)> 1:
        print(f"\n{names}'s favorite places are:")
    else:
        print(f"\n{names}'s favorite place is")
    for place in places:
        print(f"\t{place.title()}")