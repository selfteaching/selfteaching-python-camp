print("请依次输入数字a，运算符'+'or'-'or'*'or'/',数字b")
a=int(input())
x=input()
b=int(input())
if x =="+":
    c=a+b
    print(a,"+",b,"=",c)
elif x =="-":
    c=a-b
    print(a,"-",b,"=",c)
elif x =="*":
    c=a*b
    print(a,"*",b,"=",c)
elif x =="/":
    c=a/b
    print(a,"/",b,"=",c)
else:
    print("运算符号错误，请检查")