# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire document and
# count the total number of characters and display the count
# of the number of characters at the end of the document.

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

import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webaddr = input('Enter the URL of the web page to read: ')
host = re.findall('^https?://(.+)/+?',webaddr)[0]
print('Host: ',host)
try:
    mysock.connect((host,80))
except:
    print(f"Could not connect to host {host} from {webaddr}")
    print("Quitting now...")
    quit()

greq = f"GET {webaddr} HTTP/1.0\r\n\r\n".encode()
mysock.send(greq)

charsum = 0
charlimit = 3000
while True:
    data = mysock.recv(500)
    if len(data) < 1: break
    charsum += len(data)
    print(data.decode(),end='')

print(f"\nCharacters transmitted: {charsum}")
mysock.close()
