sandwich_orders = ['pastrami', 'pastrami', 'seafoods', 'pastrami', 'cheese']
finished_sandwiches = []

print("Im sorry we run out pastrami today")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:

    finished_sandwich = sandwich_orders.pop()
    
    print(f"Making your sandwich {finished_sandwich.title()}")
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f"\nI made your {sandwich}")

