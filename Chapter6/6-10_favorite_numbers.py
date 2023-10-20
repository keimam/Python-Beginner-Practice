fav_number = {
    'hadi': [17, 7, 9],
    'syarifah': [20, 3, 1],
    'alan': [69],
    'wahyu': [8, 5, 3],
    'udin': [10, 1, 5],
}

for person, number in fav_number.items():
    if len(number) > 1:
        print(f"\n{person} have more then one fav number: ")
    else:
        print(f"{person} only like one number the number is: ")
    for num in number:
        print(f"\t-{num}")