print("""欢迎使用小熊简易计算器
请选择运算方式
1.加法
2.减法
3.乘法
4.除法""") #选项菜单

choice = input("请输入1/2/3/4:")  #input 输入
a = int(input("请输入第一个数字")) #int 将输入的数值取整
b = int(input("请输入第二个数字"))

if choice == '1':
    print(a,"+",b,"=",a+b)           #if 语句中需要使用“：”，不然无法输出

elif choice == '2':
    print(a,"-",b,"=",a-b)

elif choice == "3":
    print(a,"*",b,"=",a*b)

elif choice == "4":
    print(a,"/",b,"=",a/b)

else:
    print("选择错误")

print("谢谢使用")

