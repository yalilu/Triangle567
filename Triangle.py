# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a_edge, b_edge, c_edge):
    if a_edge > 200 or b_edge > 200 or c_edge > 200:
        return 'InvalidInput'
        
    if a_edge <= 0 or b_edge <= 0 or c_edge <= 0:
        return 'InvalidInput'
    
    if not(isinstance(a_edge, int) and isinstance(b_edge, int) and isinstance(c_edge, int)):
        return 'InvalidInput'

    if (a_edge >= (b_edge + c_edge)) or (b_edge >= (a_edge + c_edge)) or (c_edge >= (a_edge + b_edge)):
        return 'NotATriangle'
        
    if a_edge == b_edge and b_edge == c_edge and a_edge == c_edge:
        return 'Equilateral'
    
    elif (a_edge * a_edge)+(b_edge * b_edge) == (c_edge * c_edge) or (a_edge * a_edge)+(c_edge * c_edge) == (b_edge*b_edge) or (c_edge * c_edge)+(b_edge * b_edge) == (a_edge * a_edge):
        return 'Right'
    
    elif (a_edge != b_edge) and  (b_edge != c_edge) and (a_edge != c_edge):
        return 'Scalene'
    
    else:
        return 'Isosceles'
