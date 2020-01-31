#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:52:49 2020

@author: lu270
"""

import math

def mysqrt(a):
    x=a/2
    while True:
        y=(x+a/x)/2
        
        if abs(y-x)<0.00000000000000001:
            return (x)
            break
        x=y
        

def test_square_root():
    header=['a','mysqrt(a)','math.sqrt(a)','diff']
    print ('{:<20s}{:<20s}{:<20s}{:<20s}'.format(header[0],header[1],header[2],header[3]))
    
    for a in range (1,10):
        x=mysqrt(a)
        y=math.sqrt(a)
        z=abs(x-y)
        lt=[a,x,y,z]
        
        
        print ('{:<20.1f}{:<20s}{:<20s}{:<20s}'.format(lt[0],str(lt[1]),str(lt[2]),str(lt[3])))
        
        
test_square_root()