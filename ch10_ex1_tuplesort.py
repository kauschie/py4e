fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print(f"File '{fname}'cannot be opened")
        exit()

d = dict()
maxemails = None
for line in fhandle:
    words = line.split()
    if (len(words) < 3) or (words[0] != 'From') or (':' in words[0]): continue
    eAddr = words[1]
    d[eAddr] = d.get(eAddr,0) + 1

elst = list()
for eAddr, count in list(d.items()):
    elst.append((count,eAddr))
elst.sort(reverse=True)
print(elst[0][1],elst[0][0])
