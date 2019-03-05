# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    # change nothing
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    # change 'b <= b'   
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    # change nothing
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    # replace '-' by '+' 
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # change a lot
    elif a == b and b == c:
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c) or ((a * a) + (c * c)) == (b * b) or\
         ((b * b) + (c * c)) == (a * a):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
