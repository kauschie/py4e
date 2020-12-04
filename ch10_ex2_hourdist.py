# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


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

hrlst = sorted(list(hrdict))
for hr in hrlst:
    print(hr, hrdict[hr])