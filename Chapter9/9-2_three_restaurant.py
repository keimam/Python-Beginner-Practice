class Restaurant:
    """class to attempt a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """Method for describing a restaurant"""
        print(f"the name of this restaurant is {self.restaurant_name}")
        print(f"the cuisine type is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Represent a information of restaurant open"""
        print(f"Restaurant {self.restaurant_name} is currently open")

my_restaurant = Restaurant('mbah uti', 'bakso')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('mang kibo', 'mie ayam')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

his_restaurant = Restaurant('mang kok', 'masakan padang')
his_restaurant.describe_restaurant()
his_restaurant.open_restaurant()