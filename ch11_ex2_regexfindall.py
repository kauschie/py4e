import re

fname = input("Enter a file: ")
try:
    fhand = open(fname)
except:
    print(f"'{fname}' is a bad filename or the program is in"
          f" the wrong directory. Quitting now...")
    quit()

count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    srch_result = re.findall('^New R.+: ([0-9]*)' , line)
    if srch_result:
        count += 1
        total += int(srch_result[0])
print(int(total/count))