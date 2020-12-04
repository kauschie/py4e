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

hrdict = dict()
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != "From": continue
    hhmmss = words[5].split(':')
    hrdict[hhmmss[0]] = hrdict.get(hhmmss[0],0) + 1

hrlst = list()
for hrMark, hrCount in list(hrdict.items()):
    hrlst.append((hrMark, hrCount))
hrlst.sort()
for hrMark, hrCount in hrlst:
    print(hrMark, hrCount)