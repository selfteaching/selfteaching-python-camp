print("<<九九乘法表>>")
for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i ,x ,i*x) ,end = '  ' )
    print('  ')
#
print('-------------------------------------------------------------')