# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:19:55 2020

@author: Happy sunday
"""

import urllib.request,urllib.parse,urllib.error
import json
import ssl


api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
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
    address = input('Enter location:')
    if len(address) < 1 :
        break
    url = serviceurl + urllib.parse.urlencode({'address':address})
    
    print('Retrieving:',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    
    try:
        js = json.load(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] !='OK':
        print('===Failure To Retrieve===')
        print(data)
        continue

    print(json.dumps(js, indent=4)) 