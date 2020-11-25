def get_numbers():
    total = 0.0
    count = 0
    inputstr = None
    while (inputstr != 'done'):
        inputstr = input('Enter a number:')
        try:
            num = float(inputstr)
        except:
            print(f"'{inputstr}' is not a number")
            print("Please enter a valid numerical input:")
            continue
        count = count + 1
        total = total + num
    print(total, count, (total/count))


get_numbers()
