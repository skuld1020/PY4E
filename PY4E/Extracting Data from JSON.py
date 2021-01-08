# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:16:24 2020

@author: Happy sunday
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_386150.json'
data = urllib.request.urlopen(url)
d = json.load(data)


l =len(d['comments'])
total = 0

for i in range(l):
    number = d['comments'][i]['count']
    total += number
print(total)

