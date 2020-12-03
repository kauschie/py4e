# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

import random

wdict = dict()
fhandle = open('words.txt')
for line in fhandle:
    words = line.split()
    for word in words:
        wdict[word] = wdict.get(word, 0) + 1
print(wdict)