class User:
    """class to define a user"""

    def __init__(self, first_name, last_name, password, location):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.location = location
        self.login_attempt = 0
    
    def describe_user(self):
        """Method to representing a user"""

        print(f"\nFirst name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"password : {self.password}")
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

hadi = User('hadi', 'suhayada', '123', 'cirebon')
hadi.increment_login_attempt()
print(hadi.login_attempt)
hadi.increment_login_attempt()
print(hadi.login_attempt)
hadi.reset_login_attempt()
print(hadi.login_attempt)