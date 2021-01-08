# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:33:51 2020

@author: Happy sunday
"""

'''打開mbox-short.txt檔案，找到所有已"From"開頭(From:不算)，
將所有的email給截取打印出來。並計算一共有幾個email'''

fname = input('Please enter a file:')
fhand = open(fname,'r')
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        email = line[1]
        print (email)
        count +=1

print('There were', count, 'lines in the file with From as the first word')