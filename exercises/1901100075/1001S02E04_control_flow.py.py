print('打印九九乘法表')#对于for...in 需要考虑缩进的问题，一般缩进以4个空格为主
for a in range(1,10):
    for b in range(1,a+1):
        print(a, '*', b, '=', a * b, sep='',  end='  ')
    print()

    #Python While 循环语句可参考https://www.runoob.com/python/python-while-loop.html
    print('用条件判断把偶数行去掉')
a=1
while a<10:
    if a%2 == 0:
        print()
    else:
        for b in range(1,a+1):
            print(a, '*',b, '=',a * b,sep='',end='  ')
    a+=1    


