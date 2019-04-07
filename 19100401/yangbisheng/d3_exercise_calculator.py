#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:23:18 2019

@author: yangbisheng
"""
def cal():
    numA = float(raw_input('Please enter a number: '))
    op = raw_input('Please enter a operator: ')
    numB = float(raw_input('Please enter another number: '))
    if op == '+':
        print "result: ",numA+numB
    elif op == '-':
        print "result: ",numA-numB
    elif op == '*':
        print "result: ",numA*numB
    elif op == '/':
        print "result: ",numA/numB
    else:
        print "Unknown operator ",op
cal()