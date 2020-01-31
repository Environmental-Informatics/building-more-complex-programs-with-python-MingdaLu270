#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:13:28 2020

@author: lu270
"""

def gcd():
    
    a=int(input('a='))
    b=int(input('b='))
    
    if a>=b:
        a,b=(a,b)
    a,b=(b,a)

    try:
        r=a%b
        
        while r != 0:
            a=b
            b=r
            r=a%b
            
        print ('GCD=',b)
        
    except ZeroDivisionError as e:
        a = e
        print('GCD=',a)

gcd()
    