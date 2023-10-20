looping = True

while looping == True:
    person = int(input("Age > "))

    if person < 2 :
        print("Baby")
        looping = True
    elif person < 4:
        print("Todler")
        looping = True
    elif person < 13:
        print("kid")
        looping = True
    elif person < 20:
        print("Teneger")
        looping = True
    elif person < 65:
        print("adult")
        looping = True
    else:
        print("You are Elder")
        break