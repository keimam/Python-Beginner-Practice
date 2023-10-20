class Restaurant:
    """class to attempt a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Method for describing a restaurant"""
        print(f"the name of this restaurant is {self.restaurant_name}")
        print(f"the cuisine type is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Represent a information of restaurant open"""
        print(f"Restaurant {self.restaurant_name} is currently open")
    
    def set_number_served(self, set_served):
        """Attempt to set number served manualy"""
        if self.number_served < set_served:
            self.number_served = set_served
        else:
            print("How can be this change to min")

class IceCreamStand(Restaurant):
    """a child class of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the icecream attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

icecream = IceCreamStand('mbak iyah', 'ice cream')
icecream.describe_restaurant()
icecream.flavors = ['choco', 'banana', 'vanilla']


for flavor in icecream.flavors:
    print(flavor)

