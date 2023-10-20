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
        self.privillage = []
    
    def show_privillages(self):
        """Method to show admin privilages"""
        if self.user_class != 'admin':
            print("The user doesn't have any privilages")
        elif self.user_class == 'admin':
            self.privillage.append('can delete post')
            self.privillage.append('can add post')
            self.privillage.append('can ban user')
            print("This is the admin privilages")
            for privillage in self.privillage:
                print(f"\t-{privillage}")


hadi = Admin('hadi', 'suhada', 'user', 'cirebon')
hadi.show_privillages()