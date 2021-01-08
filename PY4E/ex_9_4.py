# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:42:49 2020

@author: Happy sunday
"""

'''讀取mbox-short.txt並找出誰發送了最多的email
，並計算一共寄了幾次(只計算From，From:不算)'''

filename = input('Enter a file name:')
fh = open(filename,'r')
mail = dict()
largestmail = None
largesttimes = None

for line in fh:
    line = line.strip()
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        email = line[1]
        mail[email] = mail.get(email,0) + 1

#print(mail)
for k,v in mail.items():
    if largestmail == None or v > largesttimes:
        largestmail = k
        largesttimes = v

print(largestmail,largesttimes)



    