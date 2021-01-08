# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:22:36 2020

@author: Happy sunday
"""

x = int(input('Enter:'))

for i in range(1,x):
    if i % 2 ==0 and i % 3 == 0 and i % 5 !=0:
        print(i)