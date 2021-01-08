# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:43:39 2020

@author: Saahil
"""

a=int(input('Enter number'))
if a>1:
    for x in range(2,a):
        if a%x == 0:
            print('not prime')
            break
    else:
        print('prime')
else:
    print('not prime')