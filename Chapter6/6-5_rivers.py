rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'missisipi': 'usa',
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}")
print("\n")
for river in rivers.keys():
    print(f"none of biggest river {river}")
print("\n")
for country in rivers.values():
    print(f"the country has big river is {country}")