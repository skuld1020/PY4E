# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:51:11 2020

@author: Happy sunday
"""

"""利用function定義pay的金額，
40小時以內用固定rate計算，超過40小時，每小時*rate*1.5"""

def computepay(h,r):
    if h<=40:
        return h*r
    else:
        return 40*r+(h-40)*r*1.5

hrs = input('Enter Hours:')
rat = input('Enter the rate:')

try:
    hour = float(hrs)
    rate = float(rat)
except:
    print('Please enter the number for hours and rate.')
    quit()

if hour >=0 and rate>=0:
    p = computepay(hour,rate)
    print('Pay',p)
else:
    print('Please enter the real hours and rate.')