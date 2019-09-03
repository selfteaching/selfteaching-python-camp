print('..........简易计算器..........')
x = int(input("x:"))
y = int(input("y:"))
z = input("请选择，+-*/:")
if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
else:
    print(x/y)
print('..........谢谢使用..........')