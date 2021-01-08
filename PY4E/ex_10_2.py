# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:31:17 2020

@author: Happy sunday
"""

'''打開mbox-short.txt並找出'From'裡mail後面的時間，以小時為單位計算次數'''

count = dict()
hours = list()

fname = input('Please Enter a file name:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
    
fhand = open(fname,'r')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        time = line[5]
        time = time.split(':')
        hours.append(time[0])

hours.sort()

for i in hours:
    count[i] = count.get(i,0) + 1


for k,v in count.items():
    print(k,v)
    