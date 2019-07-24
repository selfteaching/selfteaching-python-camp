#通过分析，乘法口诀存在嵌套循环，
# 也就是大循环循环一次，小循环循环一遍
def cfkj(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i >= j:
                print(str(j) + "*" + str(i) + "=" + str(i*j),end=" ")
                        #j和i调换位置是为了跟现实的乘法口诀一样
                        # 第一次忘记用拼接符号+，直接报错。end是每执行一次结束空格
        print()         #循环一次之后，需要打印输出空值且换行

cfkj(9)


#for循环和while循环都可以嵌套循环

def cfkjb(y):
        a = 1      #在这里不能给b赋值，局部变量不能调用全局变量，边实践边理解
        while a <= y:
                b = 1    #局部变量不能调用全局变量
                while b <= a:                                                                       
                        print(str(a) + "*" + str(b) + "=" + str(a*b),end=(" "))
                        b = b + 1
                print()
                a = a + 1
             

cfkjb(9)

def cfkjb_1(y):
        a = 1      
        while a <= y:
                if a % 2 != 0:
                        b = 1    
                        while b <= a:                                                                       
                                print(str(a) + "*" + str(b) + "=" + str(a*b),end=(" "))
                                b = b + 1
                        print()
                a = a + 1
        #这一块语句，逗留了很久，主要问题是语句块之间的缩进和if那里想复杂了。真的验证了那一句话：缩进是python的灵魂

cfkjb_1(9)