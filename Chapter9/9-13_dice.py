from random import randint

class Die:
    """atempt a dice """

    def __init__(self, sides):
        """Initialize sides attribute"""
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)

Die6 = Die(6)
results = []

for roll in range(10):
    result = Die6.roll_die()
    results.append(result)

print(results)