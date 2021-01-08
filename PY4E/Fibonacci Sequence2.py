# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:37:00 2020

@author: Happy sunday
"""

#Fibonacci Sequence

def F(n):
    if n<=0:
        return False
    if n==1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)

Fibo =[]

s = input('Please Enter a number:')

try:
    n = int(s)
except:
    print('False')
    quit()

if n<=0:
    print('False')
else:
    for i in range(1,n+1):
        Fibo.append(F(i))
        i+=1
    print(Fibo)
    
    