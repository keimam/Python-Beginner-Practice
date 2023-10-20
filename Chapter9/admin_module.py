"""class of admin and privilages"""
from user_module import User

class Admin(User):
    """Child class of user to define an admin privilages"""
    def __init__(self, first_name, last_name, user_class, location):
        """Initialize admin privilages attributes"""
        super().__init__(first_name, last_name, user_class, location)
        self.privillage = Privillages()

class Privillages:
    """Attempt the privillages of user"""
    def __init__(self, privillages=['can ban user', 'can delete post', 'can add post']):
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
