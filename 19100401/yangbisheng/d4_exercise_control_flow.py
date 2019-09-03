# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range (1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            print("")
            break

i=0
j=0
while i<9:
    i+=1
    if i%2==0:#i等于偶数不执行后续代码
        continue
    while j<9:
        j+=1
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break



