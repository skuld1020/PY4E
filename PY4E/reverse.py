# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:11:39 2020

@author: Happy sunday
"""

'''ABC-->CBA'''

def rev(string):
    reword = list()
    n = len(string)
    for i in range(n):
        reword.append(string[n-i-1]) 
    return ''.join(reword)

x = input('Enter a word:')
print (rev(x))
        