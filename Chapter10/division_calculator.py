print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.\n")

while True:
    
    first_number = input("\nFrist Number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("can't divede by 0")
    else:    
        print(answer)
    