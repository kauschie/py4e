# Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data. Add error checking so your program does not traceback if the country code is not there. Once you have it working, search for "Atlantic Ocean" and make sure it can handle locations that are not in any country.



import urllib.request, urllib.parse, urllib.error
import json
import ssl



api_key = False
# If you have a Google Places API key, enter it here
# api_key = ''
# otherwise, api_key = False
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # Joins address with correct URL syntax
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    # gets webdata from joined url using ssl.cert=none
    uh = urllib.request.urlopen(url, context=ctx)
    # decodes byte data
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        # parses json string and loads into a dictionary
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(f"Place ID for '{address}' is {js['results'][0]['place_id']}")
