print("###############################")
print("#####欢迎来到计算中心######")
print("###############################")
a = input("请输入第一个数字: ")
print("计算方式编号如下： ")
print("1：加法 ")
print("2：减法 ")
print("3：乘法 ")
print("4：除法 ")
method = input("请选择计算方式（1/2/3/4）: ")
b = input("请输入第二个数字: ")
a = int(a)
b = int(b)
if method == "1":
    print(a+b)
elif method == "2":
    print(a-b)
elif method == "3":
    print(a*b)
elif method == "4":
    print(a/b)
else:
    print("Error")