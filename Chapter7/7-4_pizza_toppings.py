ask = True
toppings = []

while ask:
    prompt = f"\nWhat topping do you want to add? "
    prompt = f"\nEnter topping or type 'quit' to finish : "
    
    
    topping = input(prompt)

    if topping != 'quit':
        toppings.append(topping)
    else:
        print("Thank you")
        ask = False

print("You are ordered toppings : ")
for toping in toppings:
    print(f"\t-{toping}")


