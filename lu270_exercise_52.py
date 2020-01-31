#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:15:25 2020

@author: lu270
"""

def check_fermat(a,b,c,n):
    if n > 2 and a**n+b**n==c**n:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ('No, that does not work!')


def prompt():
    a = input ('a = ')
    b = input ('b = ')
    c = input ('c = ')
    n = input ('n = ')
    
    check_fermat(int(a),int(b),int(c),int(n))
    
prompt()

## raw_input works for python 2x. Tried it here but not working.