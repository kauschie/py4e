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
        num = float(inputstr)
    except:
        print(f"'{inputstr}' is not a number")
        print("Please enter a valid numerical input:")
        continue
    max = get_max(max, num)
    min = get_min(min, num)

print("All done")
print(max, min)
