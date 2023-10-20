class User:
    """class to define a user"""

    def __init__(self, first_name, last_name, user_class, location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_class = user_class
        self.location = location
        self.login_attempt = 0
    
    def describe_user(self):
        """Method to representing a user"""

        print(f"\nFirst name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"user class : {self.user_class}")
        print(f"Location : {self.location}")

    def greet_user(self):
        """method to represent a greeting to user"""
        print(f"Hi {self.first_name}")
    
    def increment_login_attempt(self):
        """Represent to login attempt"""
        self.login_attempt += 1
    
    def reset_login_attempt(self):
        """Method to reset login attempt count"""
        self.login_attempt = 0

class Admin(User):
    """Child class of user to define an admin privilages"""
    def __init__(self, first_name, last_name, user_class, location):
        """Initialize admin privilages attributes"""
        super().__init__(first_name, last_name, user_class, location)
        self.privillage = Privillages()

class Privillages:
    """Attempt the privillages of user"""
    def __init__(self, privillages=[]):
        """Initialize the attribute of privillage"""   
        self.privillages = privillages

    def show_privillages(self):
        """Method for showing privillages"""
        if self.privillages:
            print("The admin privillages show below:")
            for privillage in self.privillages:
                print(f"\t-{privillage}")
        else:
            print("The user has no privillages")
