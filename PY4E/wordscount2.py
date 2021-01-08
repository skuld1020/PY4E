# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:08:20 2020

@author: Happy sunday
"""


counts = dict()

while True:
    word = input('Enter a word:')
    if word == 'done':
        break
    if word == 'Done':
        break
    if word == 'DONE':
        break
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] +=1
    
print(counts)