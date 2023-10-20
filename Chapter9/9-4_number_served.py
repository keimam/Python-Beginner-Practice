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
    

my_restaurant = Restaurant('mbah uti', 'bakso')
print(my_restaurant.number_served)
my_restaurant.set_number_served(5)
print(my_restaurant.number_served)
