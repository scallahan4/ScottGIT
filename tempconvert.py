# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:05:52 2020

@author: Scott
"""

print("my module is running")
def fromcelcius():
    usertemp=(input("enter the tempt you want converted to degrees fahrenheit:"))
    temp=float(usertemp)
    print(type(temp))
    return((temp *1.8)+32)
def fromfahrenheit(value):
    return(value-32)/1.8