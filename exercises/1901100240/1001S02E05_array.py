#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:59:24 2019

@author: yanning
"""

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array.reverse()
str1 = ''.join(map(str,array))

str1 = str1[2:8]
str1 = str1[::-1]
int1 = int(str1)

print("The binary result is ",bin(int1))
print("The octonary result is ",oct(int1))
print("The hexadecimal result is ",hex(int1))
