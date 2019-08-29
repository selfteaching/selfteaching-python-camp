a=int(input("请输入数字："))
b=input("请输入运算符号（+ 、-、*、/）：")
c=int(input("请输入数字："))
if b=='+':
    print(a,'+',c,'=',a+c)
elif b=='-':
    print(a,'-',c,'=',a-c)
elif b=='*':
    print(a,'*',c,'=',a*c)
elif b=='/':
    print(a,'/',c,'=',a/c)
else:
    print("请重新输入")