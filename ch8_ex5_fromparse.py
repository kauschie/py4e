fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print(f"File cannot be opened: {fname}")
        exit()
fcount = 0
for line in fhandle:
    words = line.split()
    if (len(words) < 2) or (words[0] != 'From') or (':' in words[0]): continue
    print(words[1])
    fcount += 1
print(f"There were {fcount} lines in the file with From as the first word")
