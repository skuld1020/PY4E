# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:04:25 2020

@author: Happy sunday
"""

'''開起mbox-short.txt檔，
將所有X-DSPAM-Confidence後面的浮點數做出平均'''

fname = input ('Enter file name:')
fh = open(fname,'r')
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count +=1
    fstr = line.find('0')
    a = line[fstr:]
    n = float(a)
    total = total + n
    
print (total)
print (count)
aver = total / count
print (aver)