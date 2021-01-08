# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:04:25 2020

@author: Happy sunday
"""
import re

fhand = open('regex_sum_386145.txt','r')
total = 0
for line in fhand:
    line = line.rstrip()
    pat = re.compile('[0-9]+')
    num = pat.findall(line)
    
    if len(num)!=0:
        for i in range(0,len(num)):
            total += int(num[i])
            
print(total)        
        