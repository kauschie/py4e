import string


def get_file():
    fname = input("Enter a file name: ")
    try:
        fhand = open(fname)
    except:
        if fname == 'na na boo boo':
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
            exit()
        else:
            print(f"File '{fname}'cannot be opened")
            exit()
    return fhand


def get_stripped(line):
    newline_stripped = line.translate(line.maketrans("","",string.punctuation+string.digits))
    words = newline_stripped.lower().split()
    return ''.join(words)

charFrqDict = dict()
handle = get_file()
for line in handle:
    newline = get_stripped(line)
    chars = list(newline)
    for ch in chars:
        charFrqDict[ch] = charFrqDict.get(ch,0) + 1

charFrqLst = list()

for ch, count in list(charFrqDict.items()):
    charFrqLst.append((count,ch))
charFrqLst.sort(reverse=True)
for count, ch in charFrqLst:
    print(ch,count)