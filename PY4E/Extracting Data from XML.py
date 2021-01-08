# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:16:24 2020

@author: Happy sunday
"""

import urllib.request, urllib.parse, urllib.error
import xmltodict
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_386149.xml'
fd = urllib.request.urlopen(url,context=ctx).read()
data = dict(xmltodict.parse(fd,encoding='utf-8'))
total = 0
comment =data['commentinfo']['comments']['comment']
l = len(comment)

for i in range(l):
    number =int(comment[i]['count'])
    total += number
print(total)