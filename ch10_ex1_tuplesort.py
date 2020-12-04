# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
#
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.
#
# Sample Line:
#
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

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

# elst = list()
# for eAddr, count in list(d.items()):
#     elst.append((count,eAddr))
# elst.sort(reverse=True)
# print(elst[0][1],elst[0][0])

# update code to use list refactoring
elst = [(count, eAddr) for eAddr, count in d.items()]
elst.sort(reverse=True)
print(elst[0][1], elst[0][0])