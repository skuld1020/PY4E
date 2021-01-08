# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:04:25 2020

@author: Happy sunday
"""
"""大小寫轉換"""

def to_alternating_case(string):
    strn = ""
    for i in string:
        if i.isupper():
            strn += i.lower()
        else:
            strn += i.upper()
    return strn


        
x = input('Enter:')

print (to_alternating_case(x))
