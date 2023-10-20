pizzas = ['diavola', 'extravaganza', 'smoky',
          'extra cheese', 'chicken', 'spicy']

friend_pizzas = pizzas[:]

pizzas.append('Super Beef')
friend_pizzas.append('Super Limo')

print("My Fav Pizza")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy Friend Fav Pizza")
for pizza in friend_pizzas:
    print(f"- {pizza}")