def city_country(city, country):
    describe_city = f"{city} is in {country}"
    return describe_city.title()

describer = city_country('santigo', 'chile')
print(describer)
