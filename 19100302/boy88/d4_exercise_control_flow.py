#方法一
print("<<九九乘法表>>")
for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i ,x ,i*x) ,end = '  ' )
    print('  ')
#
print('-----------------------------------------------')

print("this is a new test3")
i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j < i+1:
        print(i,"*",j,"=",i*j," ",end="")
        j += 1
    print("",end="\n")
    i += 1