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


u = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))


for i in range(count):
    url = u
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup.findAll('a')
    ulist =list()
    for tag in tags:
        ulist.append(tag.get('href'))
    u = ulist[position-1]
    print(u)
        
    


