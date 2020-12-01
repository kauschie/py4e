fhand = open('romeo.txt')
wordlist = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordlist:
            wordlist.append(word)
wordlist.sort()
print(wordlist)
