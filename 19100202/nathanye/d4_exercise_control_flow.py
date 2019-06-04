# -*- coding: UTF-8 -*-

# Filename : 9*9 table
# author by : Nathanye

# 九九乘法表

for i in range(1,10): # i 代表行数
    for j in range(1,i+1): # j 代表列数
        product=i*j
        print("%d*%d=%2d\t" % (i,j,i*j),end="")
    print ()


r=1 # r 代表行数
while r<10:
    c=1 # c 代表列数
    while c<=r:
        print("%d*%d=%d\t" % (r,c,r*c),end="")
        c+=1
    print()
    r+=2
