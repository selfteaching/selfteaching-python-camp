print("1：加法 +")
print("2：减法 —")
print("3：乘法 *")
print("4：除法 /")
choice = int(input("Please input number(1/2/3/4): "))

if choice not in list(range(1,5)):
    print("输入错误！")
else:
    num1 = int(input('请输入第一个数：'))
    num2 = int(input('请输入第二个数：'))
    if choice == 1:
        print(num1,"+",num2,"=",(num1+num2))
    elif choice == 2:
        print(num1,"-",num2,"=",(num1-num2))
    elif choice == 3:
        print(num1,"*",num2,"=",(num1*num2))
    else:
        print(num1,"/",num2,"=",(num1/num2))