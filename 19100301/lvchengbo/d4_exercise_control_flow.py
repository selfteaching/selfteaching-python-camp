for n in range(1, 10):
    for x in range(1, n + 1):
            print(n, '*', x, '=', n * x)


i=1

while i < 10:    
    j=1
    while j <= i:
        print("%d*%d=%2d "%(j,i,i*j),end="")   #控制输出的格式
        j+=1
    i+=1
    print()  #打印完一行进行换行