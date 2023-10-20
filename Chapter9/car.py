"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to descirbe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neat;u formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Print a statement showing car's milage"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, milage):
        """set odometer reading to the given value"""
        if self.odometer_reading <= milage:
            self.odometer_reading = milage
        else:
            print("the odometer cant be roll back")
    
    def increment_odometer(self, miles):
        """Method to increment the odometer"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Miles cant be min")