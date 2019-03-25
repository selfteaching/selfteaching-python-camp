i = 1
while i <= 9:
    j = 1
    while i % 2 != 0 and j < i+1:#while j < i+1 这是完整的乘法口诀表
        print("%d*%d=%-2d"%(i,j,i*j),end = ' ')  
        j += 1
    print()
    i += 1