# 用来做注释的，单行哦，就是解释这个代码是什么意思

""" 多行字符串用三个引号
    包裹，也常被用来做多
    行注释
""" 


# 看了半天，似懂非懂，但是我真的想不到怎么做一个计算器咯，所以我就抄了google的，然后附上注释吧

import time  # 导入模板  时间，import是导入的意思
while 1:  #while是循环直到条件不满足为止
    print '---------------科学计算器------------'
    a=float(input('请输入第一个数字:'))   # 看不懂，
    c=raw_input('请输入+ - * /:')   # 看不懂
    d=['+','-','*','/']    
    while c not in d:
        print '算术输入格式错误请重新输入'
        c=raw_input('请输入+ - * /:')
    b=float(input('请输入第二个数字:'))    
    
    def add(d,e):    
            time.sleep(2)
            print '计算结果:',float(d+e)
            return d+e    

    def minus(f,g):
            time.sleep(2)
            print '计算结果:',float(f-g)
            return float(f-g)

    def mult(h,i):
            time.sleep(2)
            print '计算结果:',float(h*i)
            return h*i

    def chu(j,k):
            time.sleep(2)
            try:
                m=j/k
                print '计算结果:',float(m)
            except ZeroDivisionError:
                print '零不能做除数'            
    if c in d:
                
        if c=='+':
                add(a,b)          

        elif c=='/':
              chu(a,b)
            
        elif c=='-':
                minus(a,b)
        elif c=='*':
                mult(a,b)

# 哎，今天真的不知道为什么，完全没有头绪去做题，其实计算器，好像就是一个定义的过程，如果没有好的想法，真的无从下手

"""
--------------------- 
作者：月食之暗 
来源：CSDN 
原文：https://blog.csdn.net/qq_44666628/article/details/87727473 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
