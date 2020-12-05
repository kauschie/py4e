import re

count = 0
fhand = open('mbox.txt')
srch_str = input('Enter a regular expression: ')
for line in fhand:
    line = line.rstrip()
    if re.search(srch_str, line): count += 1
print(f"mbox.txt had {count} lines that matched {srch_str}")

