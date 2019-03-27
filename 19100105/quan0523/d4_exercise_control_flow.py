for x in range(1,10):    # 1<=x<10,
    for y in range(1, x+1):    # 1<=x<y<x+1
        print(x, '*', y, '=', x*y,end='\t')    # 输出所打印参数，结尾符配置为制表符\t
    print('\n')    # 由于上一行代码以制表符结尾不自动执行换行，添加换行符\n

print('\n')    # 空出来写下一段

x=1    # 为x赋值
while x<10:    # 定义x范围
    y=1    # 为y赋值
    if(x%2==1):    # 当x/2余数为1的时候
        while y<x+1:    # 定义y范围
            print(x,'*',y,'=',x*y,end='\t')   # 达到上述条件输出结果
            y=y+1    # 返回y+1
        print(end='\n')    # 当y<x+1无法实现时
        x=x+1    # 返回x+1
    else:
        x=x+1    # 当x/2余数不为1时，返回x=x+1