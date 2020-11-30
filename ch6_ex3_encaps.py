def count(xstr, xchar):
    count = 0
    for letter in xstr:
        if letter == xchar:
            count += 1
    print(count)

count('banana','a')