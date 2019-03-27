for i in range (1,10):
    for j in range (1,i+1):
        print("{}*{} = {:<4}".format(i,j,i*j),end = " ")
    print("")


row = 1        # 行数，九九乘法表有九行，因此row从1开始到9结束
while row <= 9:   
    col = 1    #列数，
    while col <= row:    # 第一行有一次输出，第二行有两次输出，.......    col < row正好符合该条件
        print("%d * %d = %d\t" % (col,row,row*col),end="")   # print() 默认每次输出都会换行，是因为默认有一个换行符\n，使用end=""，就可以不让他换行 
        col += 2
    print()     # 内层循环每循环一次都强制换行，开始下一行的输出
    row += 2