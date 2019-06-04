x=int(input("请输入第一个数"))
A=input("请输入运算符")
y=int(input("请输入第二个数"))
if A=="+":
    print(x+y)
elif A=="-":
    print(x-y)
elif A=="*":
    print(x*y)
else:
    print(x/y)

#这个程序是在网上找的一个样本，自己对照参考资料2进行了分析。
#这个程序主要是通过先设定变量，再通过设定if语句和elif语句来表述加减乘除四种变化情况下的处理方式。