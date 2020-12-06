# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.
# 
# Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL.


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

initialrecv = True
while True:
    data = mysock.recv(512).decode()
    if len(data) < 1: break
    if initialrecv:
        headerEndPos = data.find('\r\n\r\n')
        print(data[headerEndPos+4:],end='')
        initialrecv = False
    else:
        print(data,end='')

mysock.close()
