def make_car(manufacture, model, **options):
    """Make a car"""
    car_dict = {
        'manufacture': manufacture.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
    
    return car_dict

model1 = make_car('subaru', 'outback', color='blue', two_package=True)
print(model1)

model2 = make_car('toyota', 'outter', color='red', two_package=False, seater=7)
print(model2)