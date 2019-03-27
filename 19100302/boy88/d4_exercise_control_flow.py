#方法一
print("<<九九乘法表>>")
for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i ,x ,i*x) ,end = '  ' )
    print('  ')
#
print('-----------------------------------------------')
#

#方法二:
print(' 打印九九乘法表')

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print('%d X %d = %2d' %(i ,j ,i*j) ,end = '  ')
        j += 1
    i += 1
    print(' ')


print("---"* 20)
