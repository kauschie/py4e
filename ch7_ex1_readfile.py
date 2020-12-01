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
for line in fhandle:
    print(line.rstrip().upper())
