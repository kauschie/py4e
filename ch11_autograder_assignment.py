import re

try:
    fhand = open(input('Enter File Name:'))
except:
    print('Bad File name. Quitting...')
    exit()

numsum = 0
for line in fhand:
    line = line.rstrip()
    results = re.findall(('[0-9]+'),line)
    if results:
        for result in results:
            numsum += int(result)
print(numsum)