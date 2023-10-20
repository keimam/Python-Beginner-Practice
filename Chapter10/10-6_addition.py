
while True:

    try:
        num_1 = input("Input first number : ")
        if num_1 == 'q':
            break
        
        num_1 = int(num_1)

        num_2 = input("Input second number : ")
        if num_2 == 'q':
            break

        num_2 = int(num_2)

    except ValueError:
        print("input number only")
    else:
        hasil = num_1 + num_2
        print(hasil)