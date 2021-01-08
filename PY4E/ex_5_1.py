# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:29:51 2020

@author: Happy sunday
"""

"""讓使用者反覆輸入整數，直到輸入"done"為止。
輸入done後印出最大和最小的數、輸入數字次數、總和和平均。
如果使用者輸入的數字非有效數字，
使用try/except檢查並忽略此次輸入。"""

largest = None
smallest = None
count = 0
total = 0

while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        number = float(num)
    except:
        print('Please enter a real number')
        continue
    
    if largest is None and smallest is None:
        largest = number
        smallest = number
            
    if largest < number:
        largest = number
       
    if smallest > number:
        smallest = number
    
    count+=1
    total = total + number 
    

ave = total / count   
print ('Max',largest)
print('min',smallest)
print('the counts is',count)
print('the sumation is',total)
print('the average is',ave)