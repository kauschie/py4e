# Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL.

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
try:
    mysock.connect((host,80))
except:
    print(f"Could not connect to host {host} from {webaddr}")
    print("Quitting now...")
    quit()

greq = f"GET {webaddr} HTTP/1.0\r\n\r\n".encode()
mysock.send(greq)

while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode(),end='')

mysock.close()
