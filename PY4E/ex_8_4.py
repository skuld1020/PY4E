# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 03:27:06 2020

@author: Happy sunday
"""

'''打開romeo檔案，一行一行讀出，並將每個單字放到list中。
檢查每行的單字是否有在list中，若沒有，則新增。'''

filename = input('Please enter the file name:')
fh = open(filename,'r')
words = []

for line in fh:
    line = line.rstrip()
    word = line.split()
    for i in word:
        if i in words:
            continue
        else:
            words.append(i)
words =sorted(words)
print(words)

