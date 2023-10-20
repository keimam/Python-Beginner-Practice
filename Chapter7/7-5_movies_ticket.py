many_prompt = int(input("How many ticket you want to buy? "))
ask_age = 0
total_price = 0

while ask_age != many_prompt:
    age_prompt = f"How old are you ? "
    age = int(input(age_prompt))
    if age <= 3:
            ticket_price = 0
            print("The ticket is free")
            ask_age += 1
    elif age >= 3 and age <= 12:
            ticket_price = 10
            print(f"Your ticket price ${ticket_price}")
            total_price = total_price + ticket_price
            ask_age += 1
    elif age > 12:
            ticket_price = 12
            print(f"your ticket price is ${ticket_price}")
            total_price = total_price + ticket_price
            ask_age += 1

if many_prompt > 1:
    print(f"Ticket for {many_prompt} are ${total_price}")
else:
    print(f"Ticket for {many_prompt} is ${total_price}")      
