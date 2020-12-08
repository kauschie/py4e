# In this assignment you will write a Python program somewhat similar to http://
# www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML 
# data from that URL using urllib and then parse and extract the comment counts 
# from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give 
# you the sum for your testing and the other is the actual data you need to 
# process for the assignment.



import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Retrieve Web Address
address = input('Enter- ')
# address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
try:
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
except:
    print(f"Unable to retrieve data from '{address}'")
    print("Quitting now...")
    quit()

# decodes byte data
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

print(sum([int(comment.find('count').text) for comment in tree.find('comments')]))



