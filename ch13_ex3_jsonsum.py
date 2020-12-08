import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter- ')
# address = 'http://py4e-data.dr-chuck.net/comments_42.json'
try:
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
except:
    print(f"Unable to retrieve data from '{address}'")
    print("Quitting now...")
    quit()

# reads and decodes byte data
data = uh.read().decode()
print(f"Retrieved {len(data)} characters")
# loads json into dictionary
js = json.loads(data)
# print("====================================================")
# print("==============PRINTING JSON=========================")
# print(json.dumps(js, indent=4))
# print("====================================================")
# print("===================END JSON=========================")

# creates list of each['count'] using list comprehension
# then sums and prints
print(sum([ each['count'] for each in js['comments']]))