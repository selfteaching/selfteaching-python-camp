for i in range(1,10):    # for循环语句,给i赋值
    for j in range(1,i+1):
        print('%s*%s=%s'%(i,j,i*j),end = ' ')    
        # %s格式化一个对象为字符
        # end取消输出回车符，实现不换行
        # end = ' '增加空格
    
    print()