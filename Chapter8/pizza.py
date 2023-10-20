def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch of pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(12, 'pepperoni')
# make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')
