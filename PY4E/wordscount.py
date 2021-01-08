# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:08:20 2020

@author: Happy sunday
"""


counts = dict()
words = []

while True:
    word = input('Enter a word:')
    if word == 'done':
        break
    if word == 'Done':
        break
    if word == 'DONE':
        break
    else:
        words.append(word)
        
for i in words:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] +=1

print(words)
print(counts)