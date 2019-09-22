a= input("请输入运算法则（+，-，*，/）:")
b=float(input("请输入第1个数字："))
c=float (input("请输入第2个数字："))
if a=="+":
    print (b+c)
elif a=="-":
    print(b-c)
elif a=="*":
    print(b*c)
elif a=="/":
    print(b/c)
else:
    print("error")
