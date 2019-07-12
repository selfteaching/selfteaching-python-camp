for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d\t" % (i,j,i*j),end="")
    print()



row = 1
while row <= 9:
    if row % 2 != 0:   
        col = 1
        while col <= row:
            print("%d*%d=%d\t" % (row, col, row*col), end = "")
            col += 1
        print()
    row += 1
    
