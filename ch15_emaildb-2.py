# writing the program again on my own because i took a break for xmas and want to refresh my memory

import sqlite3

conn = sqlite3.connect('sql/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(email TEXT, count INTEGER)')

fname = input('Enter the filename to read: ')
if len(fname) <1: fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    # Debug
    # print('Row Before: ', row)
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?,1)', (email,))
        # Debug
        # cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
        # row = cur.fetchone()
        # print('Row After: ', row)
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
        # Debug
        # cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
        # row = cur.fetchone()
        # print('Row After: ', row)
    conn.commit()

sqlstring = cur.execute('SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10')
for row in sqlstring:
    print(row[0], row[1])

cur.close()
    
    
