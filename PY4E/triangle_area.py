# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:37:06 2020

@author: Happy sunday
"""

"""給三點求三角形邊長和面績"""

def area(a,b,c):
    s = (a+b+c)/2
    A = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return A

def length(x1,y1,x2,y2):
    L = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return L

A_x1 = input('Please input the x of A:')
A_y1 = input('Please input the y of A:')
B_x2 = input('Please input the x of B:')
B_y2 = input('Please input the y of B:')
C_x3 = input('Please input the x of C:')
C_y3 = input('Please input the y of C:')

try:
    x1 = float(A_x1)
    y1 = float(A_y1)
    x2 = float(B_x2)
    y2 = float(B_y2)
    x3 = float(C_x3)
    y3 = float(C_y3)

except:
    print('Please enter the float')
    quit()
    
    
AB = length(x1,x2,y1,y2)
BC = length(x2,x3,y2,y3)
AC = length(x1,x3,y1,y3)
A = area(AB,BC,AC)

print('A is','(',x1,',',y1,')')
print('B is','(',x2,',',y2,')')
print('C is','(',x3,',',y3,')')
print('The lengths are',AB,BC,AC)
print('The area for ABC is',A)   
