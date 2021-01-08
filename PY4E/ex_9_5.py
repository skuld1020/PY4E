# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:42:49 2020

@author: Happy sunday
"""

'''讀取mbox-short.txt並計算出各個網域名的次數
(只計算From，From:不算)'''

filename = input('Enter a file name:')
fh = open(filename,'r')
mail = dict()

for line in fh:
    line = line.strip()
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        address = line[1]
        address = address.split('@')
        a = address[1]
        mail[a] = mail.get(a,0) + 1

print(mail)



    