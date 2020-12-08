# Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data. Add error checking so your program does not traceback if the country code is not there. Once you have it working, search for "Atlantic Ocean" and make sure it can handle locations that are not in any country.



import urllib.request, urllib.parse, urllib.error
import json
import ssl

# NOTE: THIS IS MY PERSONAL API KEY FOR GOOGLE.

api_key = 'AIzaSyAf-mzcGtrGALc5ccGYwv4xWsA5kbdZt8A'
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
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

    # prints json data
    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    country_code = js['results'][0]['address_components'][-1]['short_name']
    print(location)

    # last element in address_components list always has country if it was a 
    # country that was matched

    if "country" in js['results'][0]['address_components'][-1]['types']:
        print(f"Country Code: {country_code}")
    else:
        print(f"Could not print \"{address}\"'s country code because it is"
               " not a country")
