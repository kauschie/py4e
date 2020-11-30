def get_max(current, new):
    if (current is None) or (current < new):
        return new
    else:
        return current


def get_min(current, new):
    if (current is None) or (new < current):
        return new
    else:
        return current


max = None
min = None

while True:
    inputstr = input('Enter a number:').lower()
    if inputstr == 'done':
        break
    try:
        num = int(inputstr)
    except:
        print('Invalid input')
        continue
    max = get_max(max, num)
    min = get_min(min, num)

#print("All done")
print(f"Maximum is {max}")
print(f"Minimum is {min}")
