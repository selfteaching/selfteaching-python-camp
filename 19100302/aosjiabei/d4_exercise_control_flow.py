#使用for in循环打出九九乘法表,用while循环打出奇数的九九乘法表
print("please enter'nine()' or 'mini_nine()':")
def nine():
    for i in range(1,10):
        for j in range(1,10):
            if i >= j:
                print("%d * %d = %d"%(i,j,i*j),end='\t')
        print()

def mini_nine():
    i=1
    while i<10:
        j=1
        while j<10:
            if i >= j and i%2 != 0:
                print("%d * %d = %d"%(i,j,i*j),end='\t')
            j+=1
        print()
        i+=1
        