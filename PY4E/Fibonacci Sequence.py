# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:37:00 2020

@author: Happy sunday
"""

#Fibonacci Sequence

def F(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return F(n-1)+F(n-2)
    
inp = input('Enter a interger:')
try:
     n = int(inp)
except:
    print('Please enter a interger')
    quit()

if n >=1:
    for i in range(1,n+1):
        print('The number',i,'in Fibonacci Sequence is',F(i))
        i+=1
#    print('The number',n,'in Fibonacci Sequence is',F(n))
else:
    print('No value')