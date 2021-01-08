# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:17:19 2020

@author: Happy sunday
"""

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_386147.html'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('span')
total = 0
for tag in tags:
    i = int(tag.text)
    total += i
print(total)
    


