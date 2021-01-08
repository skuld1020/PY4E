# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:17:19 2020

@author: Happy sunday
"""

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_386147.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
count = 0
for tag in tags:
    print(tag.get('href',None))
    count+=1
print(count)

