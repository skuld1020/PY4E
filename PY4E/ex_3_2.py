# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:16:27 2020

@author: Happy sunday
"""

#打印分數等及

score = input('Enter Score:')

try:
    s = float (score)
except:
    print ('Please enter your score')
    quit()


if s > 1 or s < 0:
    print ('Please enter the score between 0 and 1')
elif s >=0.9:
    print ('A')
elif s >=0.8:
    print('B')
elif s>=0.7:
    print('C')
elif s>=0.6:
    print('D')
else:
    print('F')