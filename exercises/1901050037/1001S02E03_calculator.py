
print("1.加法","2.减法","3.乘法","4.除法",sep="***",end='\n')

choice = input("(1/*/2/*/3/*/4)请输入对应功能序号:")
n1 = eval(input("请输入第一个数字:"))
n2 = eval(input("请输入第二个数字:"))

if choice == '1':
    print(n1,"+",n2,"=",n1+n2)

elif choice == '2':
    print(n1,"-",n2,"=",n1-n2)

elif choice == '3':
    print(n1,"*",n2,"=",n1*n2)

elif choice == '4':
    print(n1,"/",n2,"=",n1/n2)
else:
    print("输入错误，请重试")
pass