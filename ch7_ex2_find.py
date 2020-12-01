def get_num(nestring):
    colonpos = nestring.find(':')
    numstr = nestring[colonpos+1:]
    num = float(numstr)
    return num

fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    print(f"File cannot be opened: {fname}")
    exit()
spamcount = 0
spamtot = 0
for line in fhandle:
    if not line.lower().startswith('x-dspam-confidence:'):
        continue
    spamconf = get_num(line.rstrip())
    spamtot += spamconf
    spamcount += 1

print(f"Average spam confidence: {spamtot/spamcount}")
