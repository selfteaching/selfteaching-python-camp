opera = input("请输入符号（+,-,*,/）:")
fir_number = input("请输入第一个数字：")
sec_number = input("请输入第二个数字：")

a = int(fir_number)
b = int(sec_number)

print("opera",opera,type(opera))
print("first_number",fir_number,type(fir_number),type(a))
print("second_number",sec_number,type(sec_number),type(b))

#print("测试运算 str 加法"，fir_number + sec_number)

if opera == "+":
    print(a,"+",b,"=",a+b)
elif opera == "-":
    print(a,"-",b,"=",a-b)
elif opera == "*":
    print(a,"*",b,"=",a*b)
elif opera == "/":
    print(a,"/",b,"=",a/b)
else:
    print("无效运算")