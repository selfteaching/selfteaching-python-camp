#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:23:18 2019

@author: yangbisheng
"""
import re
def md(l,x):
    a = l.index(x)
    if x == '*' and l[a + 1] != '-':
        k = float(l[a - 1]) * float(l[a + 1])
    elif x == '/' and l[a + 1] != '-':
        k = float(l[a - 1]) / float(l[a + 1])
    elif x == '*' and l[a + 1] == '-':
        k = -(float(l[a - 1]) * float(l[a + 2]))
    elif x == '/' and l[a + 1] == '-':
        k = -(float(l[a - 1]) / float(l[a + 2]))
    del l[a - 1], l[a - 1], l[a - 1]
    l.insert(a - 1, str(k))
    return l
    print(l)
 
def fun(s):
    l = re.findall('([\d\.]+|/|-|\+|\*)',s)
    sum=0
    while 1:
        if '*' in l and '/' not in l:
            md(l, '*')
        elif '*' not in l and '/' in l:
            md(l, '/')
        elif '*' in l and '/' in l:
            a = l.index('*')
            b = l.index('/')
            if a < b:
                md(l, '*')
            else:
                md(l, '/')
        else:
            if l[0]=='-':
            l[0]=l[0]+l[1]
                del l[1]
            sum += float(l[0])
            for i in range(1, len(l), 2):
                if l[i] == '+' and l[i + 1] != '-':
                    sum += float(l[i + 1])
                elif l[i] == '+' and l[i + 1] == '-':
                    sum -= float(l[i + 2])
                elif l[i] == '-' and l[i + 1] == '-':
                    sum += float(l[i + 2])
                elif l[i] == '-' and l[i + 1] != '-':
                    sum -= float(l[i + 1])
            break
    return sum
    print(sum)
