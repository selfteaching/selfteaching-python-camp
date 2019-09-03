#使用for...in循环打印九九乘法口诀表
print('one')
for i in range(1,10): #range区间 取头不取尾 1-9;冒号不能省； 判断当i在1至a之间（即1，2,……,a）时,开始循环
    for j in range(1,i+1): #判断当j在1至i之间（即1，2,……,i）时,开始循环
        print(i,'*',j,'=',i*j,end='  ') #打印“x*y=”及其运算结果 end参数可以是空格或者制表符，不然算式全部连在一起
   
    print('')  #打印一个“换行符”即“回车”
   

#使用while循环打印九九乘法表并用条件判断除去偶数 还没完全搞懂
print('two')
x=1
y=1
while(x<10):
    while(x%2!=0):
        while(y<=x):
            print(x,'*',y,'=',x*y,'\t',end=' ')
            y=y+1
        else:
            print(end='\n')
        break
    x=x+1
    y=1


#使用for循环打印九九乘法表并用条件判断除去偶数
print('three')
for x in range(1,10):
    for y in range(1,10):
        if y<=x: #判断当y在1至y之间（即1，2,……,x）时,
            a=x*y
            if(x%2!=0): #判断当x为奇数时，执行语句
                print(x,'*',y,'=',a,end='  ')
    if(x%2!=0):
        print('  ')
