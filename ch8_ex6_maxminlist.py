numlist = list()

while True:
    inputstr = input('Enter a number: ').lower()
    if inputstr == 'done':
        break
    try:
        num = float(inputstr)
    except ValueError:
        print('Invalid input')
        continue
    numlist.append(num)

print(f"Maximum: {max(numlist)}")
print(f"Minimum: {min(numlist)}")
