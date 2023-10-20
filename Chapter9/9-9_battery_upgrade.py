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

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's size"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statment about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge")
    
    def upgrade_battery(self):
        """Try to check if battery has upgraded"""
        if self.battery_size == 40:
            self.battery_size = 65
        else:
            print("The battery has been updated")

class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car does'nt have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.battery_size = 65
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
