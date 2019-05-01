# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:25:41 2019

@author: PetalSaya
"""

def someFunction():
    pass


for x in range (1,10):
    for y in range (1, x+1):
        if x==y:
            print (x,"*",y,"=",x*y)
        else:
            print (x,"*",y,"=",x*y,end="\t")
            
i=1
while i<=9:
    j=1
    while j<=i:
        print (i,"*",j,"=",i*j,end="\t") 
        j+=1
    print()
    i+=2