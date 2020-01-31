#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:00:29 2020

@author: lu270
"""

import turtle
import math

bob=turtle.Turtle()

def arc(t,r,angle):
    arc_length=2*math.pi*r* int(angle)/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=angle/n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        

def petal (t,r,angle):
    for i in range (2):
        arc(t,r,angle)
        t.lt(180-angle)
        

def flower (t,n,r,angle):
    for i in range (n):
        petal(t,r,angle)
        t.lt(360/n)
        

def move(t,length):
    t.pu()
    t.fd(length)
    t.pd()
    
move (bob,-100)
flower(bob,7,60,60)

move (bob,100)
flower(bob,10,40,80)

move (bob,100)
flower(bob,20,140,20)

bob.hideturtle()
turtle.mainloop()


