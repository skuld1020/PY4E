# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:04:25 2020

@author: Happy sunday
"""

'''將文字末的浮點數打印出來'''

text = "X-DSPAM-Confidence:    0.8475"
a = text.find('0')
b = text.find('5')
n = text[a:]
number = float(n)
print(n)