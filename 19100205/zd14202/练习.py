#删除偶数行
i=1
while i<=9:
    k=1
    while i% 2 !=0 and k < i+1:#while k <i+1 这是完整的乘法口诀表
        print("%d*%d=%-2d"%(i,k,i*k),end ="")
        k+=1
    print()
    i+= 1
