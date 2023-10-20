class User:
    """class to define a user"""

    def __init__(self, first_name, last_name, password, location):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.location = location
    
    def describe_user(self):
        """Method to representing a user"""

        print(f"\nFirst name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"password : {self.password}")
        print(f"Location : {self.location}")

    def greet_user(self):
        """method to represent a greeting to user"""
        print(f"Hi {self.first_name}")
    

hadi = User('hadi', 'suhada', 'aaa', 'cirebon')
hadi.describe_user()
hadi.greet_user()

ari = User('ari', 'trian', 'bbb', 'cirebon')
ari.describe_user()
ari.greet_user()