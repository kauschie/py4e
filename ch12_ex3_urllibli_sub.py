# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.
#
#
# Code: http://www.py4e.com/code3/socket1.py
#
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
    # data = mysock.recv(512)
    # if len(data) < 1:
    # break
    # print(data.decode(),end='')
#
# mysock.close()

# import socket
# import re

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# webaddr = input('Enter the URL of the web page to read: ')
# host = re.findall('^https?://(.+)/+?',webaddr)[0]
# try:
#     mysock.connect((host,80))
# except:
#     print(f"Could not connect to host {host} from {webaddr}")
#     print("Quitting now...")
#     quit()

# greq = f"GET {webaddr} HTTP/1.0\r\n\r\n".encode()
# mysock.send(greq)

# charsum = 0
# charlimit = 3000
# while True:
#     data = mysock.recv(500)
#     if len(data) < 1: break
#     charsum += data
#     if charsum >= charlimit: break
#     print(data.decode(),end='')

# print(f"\nCharacters transmitted: {charsum}")
# mysock.close()

import urllib.request, urllib.parse, urllib.error

webaddr = input('Enter the web address: ')
try:
    webhandle = urllib.request.urlopen(webaddr)
except:
    print(f"Could not open web address '{webaddr}'")
    print("The link is not valid or the server is unreachable")
    print("Quitting now...")
    quit()

size = 0

while size < 3000:
    data = webhandle.read(100000)
    if len(data) < 1 : break
    size += len(data)
    print(data.decode(), end='')
    
print(f"There were {size} characters in the data")




