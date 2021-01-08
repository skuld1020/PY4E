# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:05:14 2020

@author: Happy sunday
"""

#計算40小時內每小時x元，
#超過40小時每小時加收1.5倍

hrs = input ('Enter Hours:')
h = float(hrs)
rate = input ('Enter the rate:')
r = float(rate)

if h <= 40:
    pay = h*r
else:
    pay = 40*r + (h-40)*r*1.5

print (pay)