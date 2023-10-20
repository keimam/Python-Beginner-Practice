sandwich_orders = ['pastrami', 'pastrami', 'seafoods', 'pastrami', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    
    finished_sandwich = sandwich_orders.pop()
    
    print(f"Making your sandwich {finished_sandwich.title()}")
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f"\nI made your {sandwich}")

