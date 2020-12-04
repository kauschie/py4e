# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

# takes a string and removes all punctuation and digts and spacing.
# returns the resulting string
def stripped(line):
    newline_stripped = line.translate(line.maketrans("","",string.punctuation+string.digits))
    words = newline_stripped.lower().split()
    return ''.join(words)

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

charFrqDict = dict()
for line in fhand:
    newline = stripped(line)
    chars = list(newline)
    for ch in chars:
        charFrqDict[ch] = charFrqDict.get(ch,0) + 1
        

lst = sorted([(v,k) for (k,v) in charFrqDict.items()],reverse=True)
for v,k in lst: print(k,v)
