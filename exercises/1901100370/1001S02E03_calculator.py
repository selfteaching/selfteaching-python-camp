operation=input("请输入运算符号:+,-,*,/")
print("请输入第一个数字")
a=input()
x=int(a)
print("请输入第二个数字")
b=input()
y=int(b)
print("它们的结果等于多少？")
if operation=="+":
    print(x,+'+',y,'=',x+y)
elif operation=="-":
        print(x,"-",y,'=',x-y)
elif operation=='*':
        print(x,'*',y,'=',x*y)
elif operation=='/':
        print(x,'/',y,'=',x/y)
else:
    print("您的输入有误")

    



